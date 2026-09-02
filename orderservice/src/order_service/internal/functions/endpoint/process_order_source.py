"""User-owned function implementation. The generator never overwrites this file."""

from __future__ import annotations

import asyncio
from contextvars import Token
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import uuid4

from aiohttp import web
from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult
from order_service.models.order import Order
from order_service.models.order_state import OrderState
from pyservicelib_gorundebug.datasource.http.aiohttpds import HandlerData, ResultContext
from pyservicelib_gorundebug.runtime.common import StreamContext
from pyservicelib_gorundebug.runtime.context.request import request_deadline
from pyservicelib_gorundebug.runtime.context.request import request_cancelled
from pyservicelib_gorundebug.runtime.config.endpoint_types import HttpEndpointConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment


@dataclass(slots=True)
class ProcessOrderSourceState:
    deadline_token: Token[datetime | None]
    cancellation_token: Token[asyncio.Event | None]
    cancellation: asyncio.Event
    expected_items: int = 0
    results: list[OrderItemResult] = field(default_factory=list)
    response_sent: bool = False


class ProcessOrderSource:
    """Accept orders with at least one item and positive quantities; reject malformed or invalid requests as client errors.
    Reuse X-Request-ID when supplied, otherwise generate an order ID. Preserve customer, item, price, and X-Trace data, and apply the configured timeout of five seconds by default.
    Return one response per order. When all items finish, use CONFIRMED only if every item was reserved; otherwise use PARTIALLY_CONFIRMED. If the deadline wins, return TIMED_OUT with the item results received so far.
    Calculate the total from processed item prices, falling back to the submitted total when no item result arrived, and include individual item failures in the response."""

    def __init__(self, timeout: timedelta = timedelta(seconds=5)) -> None:
        self._timeout = timeout

    async def begin_request(
        self,
        sc: StreamContext[Order, OrderState, Exception],
        data: HandlerData,
    ) -> tuple[HandlerData, ProcessOrderSourceState]:
        del sc
        deadline = datetime.now(timezone.utc) + self._timeout
        deadline_token = request_deadline.set(deadline)
        cancellation = asyncio.Event()
        cancellation_token = request_cancelled.set(cancellation)
        return data, ProcessOrderSourceState(
            deadline_token=deadline_token,
            cancellation_token=cancellation_token,
            cancellation=cancellation,
        )

    async def consume_message(
        self,
        sc: StreamContext[Order, OrderState, Exception],
        handler_state: ProcessOrderSourceState,
        data: HandlerData,
        result_ctx: ResultContext[ProcessOrderSourceState, Order, OrderState, Exception],
    ) -> None:
        body = await data.request.json()
        if not isinstance(body, dict):
            raise web.HTTPBadRequest(text="JSON body must be an object\n")

        raw_items = body.get("items")
        if not isinstance(raw_items, list) or not raw_items:
            raise web.HTTPBadRequest(text="items must not be empty\n")

        order_id = data.request.headers.get("X-Request-ID") or str(uuid4())
        items: list[OrderItem] = []
        total_amount = 0.0
        for raw_item in raw_items:
            if not isinstance(raw_item, dict):
                raise web.HTTPBadRequest(text="each item must be an object\n")
            quantity = int(_field(raw_item, "quantity"))
            if quantity <= 0:
                raise web.HTTPBadRequest(text="all quantities must be positive\n")
            unit_price = float(_field(raw_item, "unitPrice", "unit_price", default=0.0))
            item = OrderItem(
                order_id=order_id,
                item_id=str(_field(raw_item, "itemId", "item_id")),
                sku=str(_field(raw_item, "sku")),
                quantity=quantity,
                unit_price=unit_price,
            )
            items.append(item)
            total_amount += quantity * unit_price

        handler_state.expected_items = len(items)
        order = Order(
            id=order_id,
            customer_id=str(_field(body, "customerId", "customer_id", default="")),
            items=items,
            total_amount=total_amount,
            created_at=datetime.now(timezone.utc),
            trace_id=data.request.headers.get("X-Trace", ""),
        )

        def on_result(
            sc: StreamContext[Order, OrderState, Exception],
            handler_state: ProcessOrderSourceState,
            value: OrderState,
            data: HandlerData,
        ) -> bool:
            del sc
            if handler_state.response_sent:
                return True

            if value.status != "TIMED_OUT":
                handler_state.results.extend(value.confirmed_items)
                if len(handler_state.results) < handler_state.expected_items:
                    return False

            status = value.status
            if status != "TIMED_OUT":
                status = (
                    "CONFIRMED"
                    if all(result.reserved for result in handler_state.results)
                    else "PARTIALLY_CONFIRMED"
                )

            total = sum(
                result.unit_price * result.requested_qty for result in handler_state.results
            )
            if not handler_state.results:
                total = order.total_amount
            response: dict[str, object] = {
                "order_id": order.id,
                "status": status,
                "total_amount": total,
                "processed_at": datetime.now(timezone.utc).isoformat(),
            }
            if handler_state.results:
                response["confirmed_items"] = [
                    {
                        "item_id": result.item_id,
                        "sku": result.sku,
                        "available_qty": result.available_qty,
                        "reserved": result.reserved,
                        "status": result.status,
                        **({"error": result.error} if result.error else {}),
                    }
                    for result in handler_state.results
                ]
            data.set_response(web.json_response(response))
            handler_state.response_sent = True
            result_ctx.done()
            return True

        result_ctx.set_result_callback(order_id, on_result)
        await sc.collect(order)

    def get_message_id(
        self,
        sc: StreamContext[Order, OrderState, Exception],
        handler_state: ProcessOrderSourceState,
        value: OrderState,
    ) -> str:
        del sc, handler_state
        return value.order_id

    async def end_request(
        self,
        sc: StreamContext[Order, OrderState, Exception],
        err: Exception | None,
        handler_state: ProcessOrderSourceState,
        data: HandlerData,
    ) -> None:
        del sc
        handler_state.cancellation.set()
        request_cancelled.reset(handler_state.cancellation_token)
        request_deadline.reset(handler_state.deadline_token)
        if err is not None and not data._response.done():
            data.set_response(
                web.json_response(
                    {"error": "internal server error"},
                    status=500,
                )
            )


_MISSING = object()


def _field(
    obj: dict[str, Any],
    *names: str,
    default: object = _MISSING,
) -> Any:
    for name in names:
        if name in obj:
            return obj[name]
    if default is not _MISSING:
        return default
    raise web.HTTPBadRequest(text=f"missing field: {names[0]}")


async def make_process_order_source(
    ctx: Context, environment: ServiceEnvironment, config: HttpEndpointConfig
) -> ProcessOrderSource:
    del ctx, environment
    timeout_ms = config.get_property("timeout")
    if timeout_ms is None:
        timeout_ms = 5000
    return ProcessOrderSource(timeout=timedelta(milliseconds=float(timeout_ms)))
