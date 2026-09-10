"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class AdvanceCycleAnalytics:
    """Increment the cycle counter while preserving the analytics event identity."""

    async def map(
        self,
        stream: Stream,
        value: AnalyticsEvent,
        out: Collect[AnalyticsEvent],
    ) -> None:
        del stream
        await out.out(AnalyticsEvent(key=value.key, value=value.value + 1, kind=value.kind))


async def make_advance_cycle_analytics(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> AdvanceCycleAnalytics:
    """Construct AdvanceCycleAnalytics asynchronously while the graph is initialized."""
    del ctx, config, environment
    return AdvanceCycleAnalytics()
