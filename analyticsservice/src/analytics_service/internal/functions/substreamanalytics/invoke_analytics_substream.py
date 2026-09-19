"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import (
    Collect,
    Stream,
    SubStream,
    SubStreamCollectorFunc,
)
class InvokeAnalyticsSubstream:
    """Invoke the service-local analytics SubStream and emit its returned result."""

    def __init__(self, substream: SubStream[AnalyticsEvent, AnalyticsResult]) -> None:
        self._substream = substream

    async def map(
        self,
        stream: Stream,
        value: AnalyticsEvent,
        out: Collect[AnalyticsResult],
    ) -> None:
        del stream

        async def collect(result: AnalyticsResult) -> bool:
            await out.out(result)
            return True

        await self._substream.consume(value, SubStreamCollectorFunc(collect))


async def make_invoke_analytics_substream(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> InvokeAnalyticsSubstream:
    """Construct InvokeAnalyticsSubstream asynchronously while the graph is initialized."""
    del ctx, config, environment
    raise RuntimeError(
        "InvokeAnalyticsSubstream must be constructed by Service.custom_makers_init "
        "with the analyzeAnalyticsSubstream handle"
    )
