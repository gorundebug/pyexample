"""Generated test for the service extension lifecycle."""

import pytest

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from analytics_service.internal.app.service import Service
from analytics_service.internal.config import Config
from analytics_service.internal.functions import CountOrderProcessed


class _RecordingService(Service):
    def __init__(self) -> None:
        super().__init__()
        self.events: list[str] = []

    async def custom_makers_init(self, ctx: Context) -> None:
        await super().custom_makers_init(ctx)
        self.events.append("custom_makers_init")
        original_maker = self.makers.count_order_processed

        async def make_function(
            ctx: Context, env: ServiceEnvironment
        ) -> CountOrderProcessed:
            self.events.append("function_maker")
            return await original_maker(ctx, env)

        self.makers.count_order_processed = make_function

    async def custom_functions_init(self, ctx: Context) -> None:
        await super().custom_functions_init(ctx)
        assert isinstance(self.functions.count_order_processed, CountOrderProcessed)
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
    assert isinstance(service.functions.count_order_processed, CountOrderProcessed)