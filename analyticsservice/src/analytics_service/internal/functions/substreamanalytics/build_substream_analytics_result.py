"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream
class BuildSubstreamAnalyticsResult:
    """Transform one callable SubStream input into its analytics result."""

    async def map(
        self,
        stream: Stream,
        value: AnalyticsEvent,
        out: Collect[AnalyticsResult],
    ) -> None:
        del stream
        await out.out(AnalyticsResult(
            key=value.key,
            total=value.value * 2,
            kind="substream",
        ))


async def make_build_substream_analytics_result(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> BuildSubstreamAnalyticsResult:
    """Construct BuildSubstreamAnalyticsResult asynchronously while the graph is initialized."""
    del ctx, config, environment
    return BuildSubstreamAnalyticsResult()
