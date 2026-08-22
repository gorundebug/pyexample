"""Generated test for the service extension lifecycle."""

import pytest

from pyservicelib_gorundebug.runtime.context.context import Context

from analytics_service.internal.app.service_generated import GeneratedService
from analytics_service.internal.config import Config


class _Function:
    pass


class _RecordingService(GeneratedService):
    def __init__(self) -> None:
        super().__init__()
        self.events: list[str] = []

    async def custom_makers_init(self, ctx: Context) -> None:
        del ctx
        self.events.append("custom_makers_init")
        self.makers.count_order_processed = lambda ctx, env, cfg: _Function()

    async def custom_functions_init(self, ctx: Context) -> None:
        del ctx
        assert isinstance(self.functions.count_order_processed, _Function)
        self.events.append("custom_functions_init")


@pytest.mark.asyncio
async def test_generated_function_hook_order() -> None:
    service = _RecordingService()
    config = Config.from_dict({})
    assert config is not None
    service.set_config(config)
    await service.initialize_functions(Context())
    assert service.events == ["custom_makers_init", "custom_functions_init"]
    assert isinstance(service.functions.count_order_processed, _Function)