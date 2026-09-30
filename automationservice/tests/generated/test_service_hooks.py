"""Generated test for the service extension lifecycle."""

import pytest

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from automation_service.internal.app.service import Service
from automation_service.internal.config import Config
from automation_service.internal.functions import ActivityJobEndpointSink


class _RecordingService(Service):
    def __init__(self) -> None:
        super().__init__()
        self.events: list[str] = []

    async def custom_makers_init(self, ctx: Context) -> None:
        await super().custom_makers_init(ctx)
        self.events.append("custom_makers_init")
        original_maker = self.makers.activity_job_endpoint_sink

        async def make_function(
            ctx: Context, env: ServiceEnvironment
        ) -> ActivityJobEndpointSink:
            self.events.append("function_maker")
            return await original_maker(ctx, env)

        self.makers.activity_job_endpoint_sink = make_function

    async def custom_functions_init(self, ctx: Context) -> None:
        await super().custom_functions_init(ctx)
        assert isinstance(self.functions.activity_job_endpoint_sink, ActivityJobEndpointSink)
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
    assert isinstance(service.functions.activity_job_endpoint_sink, ActivityJobEndpointSink)