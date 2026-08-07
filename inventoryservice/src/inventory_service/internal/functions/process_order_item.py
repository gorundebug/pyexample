"""User-owned function implementation. The generator never overwrites this file."""
import asyncio

from inventory_service_api.generated.proto.inventoryserviceapi.processorderitem.processorderitem_pb2 import ProcessOrderItemRequest, ProcessOrderItemResponse
from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.datasource.grpc.grpcds import ResultContext, Sender
from pyservicelib_gorundebug.runtime.common import StreamContext


class ProcessOrderItem:
    """Outgoing unary gRPC call to the Inventory Service.
[ConsumeMessage] map OrderItem → ProcessOrderItemRequest (OrderID, ItemID, SKU, Quantity); call sender.Send(req).
[HandleResponse] map ProcessOrderItemResponse → OrderItemResult:
copy OrderID, ItemID, AvailableQty, Reserved, Status, UnitPrice from response; push downstream via sc.Collect.
[EndRequest] log the outcome."""

    async def begin_request(
        self,
        sc: StreamContext[OrderItem, OrderItemResult, Exception],
    ) -> None:
        del sc
        return None

    async def consume_message(
        self,
        sc: StreamContext[OrderItem, OrderItemResult, Exception],
        handler_state: None,
        request: ProcessOrderItemRequest,
        result_ctx: ResultContext[
            None, OrderItem, ProcessOrderItemResponse, OrderItemResult, Exception
        ],
        sender: Sender[ProcessOrderItemResponse],
    ) -> None:
        del handler_state
        item = OrderItem(
            order_id=request.order_id,
            item_id=request.item_id,
            sku=request.sku,
            quantity=request.quantity,
        )

        def send_result(
            sc: StreamContext[OrderItem, OrderItemResult, Exception],
            handler_state: None,
            value: OrderItemResult,
            sender: Sender[ProcessOrderItemResponse],
        ) -> bool:
            del sc, handler_state
            async def send_and_finish() -> None:
                await sender.send(
                    ProcessOrderItemResponse(
                        available_qty=value.available_qty,
                        reserved=value.reserved,
                        status=value.status,
                    )
                )
                result_ctx.done()

            asyncio.create_task(send_and_finish())
            return True

        result_ctx.set_result_callback(request.item_id, send_result)
        await sc.collect(item)

    def get_message_id(
        self,
        sc: StreamContext[OrderItem, OrderItemResult, Exception],
        handler_state: None,
        value: OrderItemResult,
    ) -> str:
        del sc, handler_state
        return value.item_id

    def eof(
        self,
        sc: StreamContext[OrderItem, OrderItemResult, Exception],
        handler_state: None,
    ) -> None:
        del sc, handler_state

    async def end_request(
        self,
        sc: StreamContext[OrderItem, OrderItemResult, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del sc, err, handler_state
