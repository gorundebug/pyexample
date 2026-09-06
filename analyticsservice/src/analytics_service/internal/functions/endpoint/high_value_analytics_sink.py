"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import CustomEndpointConfig
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import Collect, TypedSinkStream


class HighValueAnalyticsSink:
    """Validate and record analytics results routed to the high-value Case branch."""

    def get_stream_id(self, ctx: Context, value: AnalyticsResult) -> str:
        del ctx, value
        return ""

    async def begin_request(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsResult, Exception],
    ) -> tuple[Context, None]:
        del stream
        return ctx, None

    async def consume_message(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsResult, Exception],
        handler_state: None,
        value: AnalyticsResult,
        result_stream: Collect[Exception],
    ) -> None:
        del ctx, stream, handler_state, result_stream
        if value != AnalyticsResult(key="high-value", total=60, kind="multi"):
            raise ValueError(f"unexpected high-value analytics result: {value!r}")

    async def end_request(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsResult, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del ctx, stream, err, handler_state


async def make_high_value_analytics_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CustomEndpointConfig,
) -> HighValueAnalyticsSink:
    """Construct HighValueAnalyticsSink asynchronously while the graph is initialized."""
    del ctx, config, environment
    return HighValueAnalyticsSink()
