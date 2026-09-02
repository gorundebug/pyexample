"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.endpoint_types import GrpcEndpointConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from inventory_service_api.generated.proto.inventoryserviceapi.processorderitem.processorderitem_pb2 import (
    ProcessOrderItemRequest,
    ProcessOrderItemResponse,
)
from model.models.order_item import OrderItem
from model.models.order_item_result import OrderItemResult
from pyservicelib_gorundebug.datasource.grpc.grpcds import ResultContext, Sender
from pyservicelib_gorundebug.runtime.common import StreamContext


class ProcessOrderItemSource:
    """Reserve inventory for one order item using its order ID, item ID, SKU, and quantity.
    Return the available quantity, reservation outcome, and status. The caller combines this response with the original identity, requested quantity, and unit price.
    If the inventory call fails, the caller returns a non-reserved PROCESSING_ERROR result with the failure message."""

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

        async def send_result(
            sc: StreamContext[OrderItem, OrderItemResult, Exception],
            handler_state: None,
            value: OrderItemResult,
            sender: Sender[ProcessOrderItemResponse],
        ) -> bool:
            del sc, handler_state

            await sender.send(
                ProcessOrderItemResponse(
                    available_qty=value.available_qty,
                    reserved=value.reserved,
                    status=value.status,
                )
            )
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


async def make_process_order_item_source(
    ctx: Context, environment: ServiceEnvironment, config: GrpcEndpointConfig
) -> ProcessOrderItemSource:
    del ctx, environment, config
    return ProcessOrderItemSource()
