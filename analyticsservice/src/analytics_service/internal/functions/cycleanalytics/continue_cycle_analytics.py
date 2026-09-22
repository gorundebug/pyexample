"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from analytics_service.models.analytics_event import AnalyticsEvent
from pyservicelib_gorundebug.runtime.common import Stream


class ContinueCycleAnalytics:
    """Keep intermediate analytics events whose cycle counter is below three."""

    async def filter(self, stream: Stream, value: AnalyticsEvent) -> bool:
        del stream
        return value.value < 3


async def make_continue_cycle_analytics(
    ctx: Context,
    environment: ServiceEnvironment,
) -> ContinueCycleAnalytics:
    """Construct ContinueCycleAnalytics asynchronously while the graph is initialized."""
    del ctx, environment
    return ContinueCycleAnalytics()
