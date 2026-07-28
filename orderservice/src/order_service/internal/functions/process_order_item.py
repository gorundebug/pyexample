"""User-owned function implementation. The generator never overwrites this file."""
from dataclasses import dataclass

from inventory_service_api.generated.proto.inventoryserviceapi.processorderitem.processorderitem_pb2 import ProcessOrderItemRequest, ProcessOrderItemResponse
from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.datasink.grpc.grpcds import ResultContext, Sender
from pyservicelib_gorundebug.runtime.common import SinkStreamContext


class ProcessOrderItem:
    """Outgoing unary gRPC call to the Inventory Service.
[ConsumeMessage] map OrderItem → ProcessOrderItemRequest (OrderID, ItemID, SKU, Quantity); call sender.Send(req).
[HandleResponse] map ProcessOrderItemResponse → OrderItemResult:
copy OrderID, ItemID, AvailableQty, Reserved, Status, UnitPrice from response; push downstream via sc.Collect.
[EndRequest] log the outcome."""

    @dataclass(slots=True)
    class State:
        order_id: str = ""
        item_id: str = ""
        sku: str = ""
        requested_qty: int = 0
        unit_price: float = 0.0

    async def begin_request(
        self,
        sc: SinkStreamContext[OrderItem, OrderItemResult, Exception],
    ) -> State:
        del sc
        return self.State()

    async def consume_message(
        self,
        sc: SinkStreamContext[OrderItem, OrderItemResult, Exception],
        handler_state: State,
        value: OrderItem,
        sender: Sender[ProcessOrderItemRequest],
        result_ctx: ResultContext,
    ) -> None:
        del sc, result_ctx
        handler_state.order_id = value.order_id
        handler_state.item_id = value.item_id
        handler_state.sku = value.sku
        handler_state.requested_qty = value.quantity
        handler_state.unit_price = value.unit_price
        await sender.send(
            ProcessOrderItemRequest(
                order_id=value.order_id,
                item_id=value.item_id,
                sku=value.sku,
                quantity=value.quantity,
            )
        )

    async def handle_response(
        self,
        sc: SinkStreamContext[OrderItem, OrderItemResult, Exception],
        handler_state: State,
        response: ProcessOrderItemResponse,
    ) -> None:
        await sc.collect(
            OrderItemResult(
                order_id=handler_state.order_id,
                item_id=handler_state.item_id,
                sku=handler_state.sku,
                requested_qty=handler_state.requested_qty,
                available_qty=response.available_qty,
                reserved=response.reserved,
                status=response.status,
                unit_price=handler_state.unit_price,
            )
        )

    async def end_request(
        self,
        sc: SinkStreamContext[OrderItem, OrderItemResult, Exception],
        err: Exception | None,
        handler_state: State,
    ) -> None:
        del sc, err, handler_state
