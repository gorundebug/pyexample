"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MultiJoinStreamConfig
from typing import Any
from analytics_service.models.analytics_event import AnalyticsEvent
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class MultiJoinAnalyticsEvents:
    """Combine matching order, payment, and shipment analytics events."""

    async def multi_join(
        self,
        stream: Stream,
        key: str,
        values: list[list[Any]],
        out: Collect[AnalyticsResult],
    ) -> bool:
        del stream
        if len(values) != 3 or any(not group for group in values):
            return False
        order, payment, shipment = values[0][0], values[1][0], values[2][0]
        if not all(isinstance(value, AnalyticsEvent) for value in (order, payment, shipment)):
            return False
        await out.out(
            AnalyticsResult(
                key=key,
                total=order.value + payment.value + shipment.value,
                kind="multi",
            )
        )
        return True


async def make_multi_join_analytics_events(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MultiJoinStreamConfig,
) -> MultiJoinAnalyticsEvents:
    """Construct MultiJoinAnalyticsEvents asynchronously while the graph is initialized."""
    del ctx, config, environment
    return MultiJoinAnalyticsEvents()
