"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import JoinStreamConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class JoinOrderPaymentAnalytics:
    """Join matching order and payment analytics events and emit their combined total."""

    async def join(
        self,
        stream: Stream,
        key: str,
        left_values: list[AnalyticsEvent],
        right_values: list[AnalyticsEvent],
        out: Collect[AnalyticsResult],
    ) -> bool:
        del stream
        if not left_values or not right_values:
            return False
        await out.out(
            AnalyticsResult(
                key=key,
                total=left_values[0].value + right_values[0].value,
                kind="join",
            )
        )
        return True


async def make_join_order_payment_analytics(
    ctx: Context,
    environment: ServiceEnvironment,
    config: JoinStreamConfig,
) -> JoinOrderPaymentAnalytics:
    """Construct JoinOrderPaymentAnalytics asynchronously while the graph is initialized."""
    del ctx, config, environment
    return JoinOrderPaymentAnalytics()
