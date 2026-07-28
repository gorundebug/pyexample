"""Generated gRPC server adapter. DO NOT EDIT."""
from typing import Any, cast

import grpc

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment.environment import Lifecycle
import inventory_service_api.generated.proto.inventoryserviceapi.inventoryserviceapi.generated_pb2_grpc as grpc_api_1
import inventory_service_api.generated.proto.inventoryserviceapi.processorderitem.processorderitem_pb2 as grpc_messages_4


class _InventoryServiceApiServicer(grpc_api_1.InventoryServiceApiServicer):
    def __init__(self, handlers: dict[int, Any]) -> None:
        self._handler_4 = handlers[4]


    async def ProcessOrderItem(
        self,
        request: grpc_messages_4.ProcessOrderItemRequest,
        context: grpc.aio.ServicerContext[
            grpc_messages_4.ProcessOrderItemRequest,
            grpc_messages_4.ProcessOrderItemResponse,
        ],
    ) -> grpc_messages_4.ProcessOrderItemResponse:
        return cast(
            grpc_messages_4.ProcessOrderItemResponse,
            await self._handler_4(request, context),
        )


class GrpcServer(Lifecycle):
    def __init__(
        self,
        host: str,
        port: int,
        handlers: dict[int, Any],
    ) -> None:
        self._server = grpc.aio.server()
        grpc_api_1.add_InventoryServiceApiServicer_to_server(  # type: ignore[no-untyped-call]
            _InventoryServiceApiServicer(handlers),
            self._server,
        )
        self._server.add_insecure_port(f"{host}:{port}")

    async def start(self, ctx: Context) -> None:
        del ctx
        await self._server.start()

    async def stop(self, ctx: Context) -> None:
        await self._server.stop(grace=ctx.time_left)