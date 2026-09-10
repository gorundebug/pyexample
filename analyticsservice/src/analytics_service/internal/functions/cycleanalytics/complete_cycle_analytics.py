"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import FilterStreamConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from pyservicelib_gorundebug.runtime.common import Stream


class CompleteCycleAnalytics:
    """Keep the terminal analytics event once its cycle counter reaches three."""

    async def filter(self, stream: Stream, value: AnalyticsEvent) -> bool:
        del stream
        return value.value >= 3


async def make_complete_cycle_analytics(
    ctx: Context,
    environment: ServiceEnvironment,
    config: FilterStreamConfig,
) -> CompleteCycleAnalytics:
    """Construct CompleteCycleAnalytics asynchronously while the graph is initialized."""
    del ctx, config, environment
    return CompleteCycleAnalytics()
