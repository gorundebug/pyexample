"""Generated gRPC server adapter. DO NOT EDIT."""
from typing import Any, cast

import grpc

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment.environment import Lifecycle
import inventory_service_api.generated.proto.inventoryserviceapi.inventoryserviceapi.generated_pb2_grpc as inventory_service_api_grpc_api
import inventory_service_api.generated.proto.inventoryserviceapi.processorderitem.processorderitem_pb2 as process_inventory_item_grpc_messages


class _InventoryServiceApiServicer(inventory_service_api_grpc_api.InventoryServiceApiServicer):
    def __init__(self, handlers: dict[str, Any]) -> None:
        self._process_inventory_item_handler = handlers["process_inventory_item"]


    async def ProcessOrderItem(
        self,
        request: process_inventory_item_grpc_messages.ProcessOrderItemRequest,
        context: grpc.aio.ServicerContext[
            process_inventory_item_grpc_messages.ProcessOrderItemRequest,
            process_inventory_item_grpc_messages.ProcessOrderItemResponse,
        ],
    ) -> process_inventory_item_grpc_messages.ProcessOrderItemResponse:
        return cast(
            process_inventory_item_grpc_messages.ProcessOrderItemResponse,
            await self._process_inventory_item_handler(request, context),
        )


class GrpcServer(Lifecycle):
    def __init__(
        self,
        host: str,
        port: int,
        handlers: dict[str, Any],
    ) -> None:
        self._server = grpc.aio.server()
        inventory_service_api_grpc_api.add_InventoryServiceApiServicer_to_server(  # type: ignore[no-untyped-call]
            _InventoryServiceApiServicer(handlers),
            self._server,
        )
        self._server.add_insecure_port(f"{host}:{port}")

    async def start(self, ctx: Context) -> None:
        del ctx
        await self._server.start()

    async def stop(self, ctx: Context) -> None:
        await self._server.stop(grace=ctx.time_left)