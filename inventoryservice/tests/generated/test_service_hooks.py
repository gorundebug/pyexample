"""Generated test for the service extension lifecycle."""

import pytest

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import GrpcEndpointConfig

from inventory_service.internal.app.service_generated import GeneratedService
from inventory_service.internal.config import Config
from inventory_service.internal.functions import ProcessOrderItemSource


class _RecordingService(GeneratedService):
    def __init__(self) -> None:
        super().__init__()
        self.events: list[str] = []

    async def custom_makers_init(self, ctx: Context) -> None:
        del ctx
        self.events.append("custom_makers_init")
        original_maker = self.makers.process_order_item_source

        async def make_function(
            ctx: Context, env: ServiceEnvironment, cfg: GrpcEndpointConfig
        ) -> ProcessOrderItemSource:
            self.events.append("function_maker")
            return await original_maker(ctx, env, cfg)

        self.makers.process_order_item_source = make_function

    async def custom_functions_init(self, ctx: Context) -> None:
        del ctx
        assert isinstance(self.functions.process_order_item_source, ProcessOrderItemSource)
        self.events.append("custom_functions_init")


@pytest.mark.asyncio
async def test_generated_function_hook_order() -> None:
    service = _RecordingService()
    config = Config.from_dict({})
    assert config is not None
    service.set_config(config)
    await service.initialize_functions(Context())
    assert service.events == [
        "custom_makers_init",
        "function_maker",
        "custom_functions_init",
    ]
    assert isinstance(service.functions.process_order_item_source, ProcessOrderItemSource)
