"""Behavior tests for the user-owned ProcessOrderSource handler."""

from __future__ import annotations

import json
from typing import Any

import pytest
from aiohttp import web
from model.models.order_item_result import OrderItemResult
from order_service.internal.functions.endpoint.process_order_source import ProcessOrderSource
from order_service.models.order_state import OrderState


class Request:
    def __init__(self, body: object) -> None:
        self._body = body
        self.headers = {"X-Request-ID": "order-1", "X-Trace": "trace-1"}

    async def json(self) -> object:
        return self._body


class Data:
    def __init__(self, body: object) -> None:
        self.request = Request(body)
        self.response: Any = None

    def set_response(self, response: Any) -> None:
        self.response = response


class StreamContext:
    def __init__(self) -> None:
        self.values: list[Any] = []

    async def collect(self, value: Any) -> None:
        self.values.append(value)


class ResultContext:
    def __init__(self) -> None:
        self.callback: Any = None
        self.done_called = False

    def set_result_callback(self, message_id: str, callback: Any) -> None:
        assert message_id == "order-1"
        self.callback = callback

    def done(self) -> None:
        self.done_called = True


@pytest.mark.asyncio
async def test_process_order_source_aggregates_results_into_openapi_response() -> None:
    function = ProcessOrderSource()
    stream = StreamContext()
    data = Data(
        {
            "customer_id": "customer-1",
            "items": [
                {
                    "item_id": "item-1",
                    "sku": "SKU-001",
                    "quantity": 2,
                    "unit_price": 3.5,
                },
                {
                    "item_id": "item-2",
                    "sku": "UNKNOWN",
                    "quantity": 1,
                    "unit_price": 7.0,
                },
            ],
        }
    )
    result = ResultContext()
    _, state = await function.begin_request(stream, data)  # type: ignore[arg-type]

    await function.consume_message(  # type: ignore[arg-type]
        stream, state, data, result
    )

    assert len(stream.values) == 1
    order = stream.values[0]
    assert order.id == "order-1"
    assert order.total_amount == 14.0
    assert result.callback is not None

    first_done = result.callback(
        stream,
        state,
        OrderState(
            order_id="order-1",
            status="CONFIRMED",
            confirmed_items=[
                OrderItemResult(
                    order_id="order-1",
                    item_id="item-1",
                    sku="SKU-001",
                    requested_qty=2,
                    available_qty=2,
                    reserved=True,
                    status="CONFIRMED",
                    unit_price=3.5,
                )
            ],
        ),
        data,
    )
    assert first_done is False
    assert result.done_called is False

    second_done = result.callback(
        stream,
        state,
        OrderState(
            order_id="order-1",
            status="PARTIALLY_CONFIRMED",
            confirmed_items=[
                OrderItemResult(
                    order_id="order-1",
                    item_id="item-2",
                    sku="UNKNOWN",
                    requested_qty=1,
                    available_qty=0,
                    reserved=False,
                    status="OUT_OF_STOCK",
                    unit_price=7.0,
                )
            ],
        ),
        data,
    )

    assert second_done is True
    assert result.done_called is True
    payload = json.loads(data.response.text)
    assert payload == {
        "order_id": "order-1",
        "status": "PARTIALLY_CONFIRMED",
        "confirmed_items": [
            {
                "item_id": "item-1",
                "sku": "SKU-001",
                "available_qty": 2,
                "reserved": True,
                "status": "CONFIRMED",
            },
            {
                "item_id": "item-2",
                "sku": "UNKNOWN",
                "available_qty": 0,
                "reserved": False,
                "status": "OUT_OF_STOCK",
            },
        ],
        "total_amount": 14.0,
        "processed_at": payload["processed_at"],
    }

    await function.end_request(stream, None, state, data)  # type: ignore[arg-type]


@pytest.mark.asyncio
async def test_process_order_source_rejects_empty_items() -> None:
    function = ProcessOrderSource()
    stream = StreamContext()
    data = Data({"items": []})
    result = ResultContext()
    _, state = await function.begin_request(stream, data)  # type: ignore[arg-type]

    with pytest.raises(web.HTTPBadRequest) as error:
        await function.consume_message(  # type: ignore[arg-type]
            stream, state, data, result
        )
    assert error.value.text == "items must not be empty\n"

    await function.end_request(stream, None, state, data)  # type: ignore[arg-type]
