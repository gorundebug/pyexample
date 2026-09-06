"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import CustomEndpointConfig
from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import Collect, TypedSinkStream


class StandardAnalyticsSink:
    """Validate and record analytics results routed to the standard Case branch."""

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
        if value != AnalyticsResult(key="standard", total=6, kind="multi"):
            raise ValueError(f"unexpected standard analytics result: {value!r}")

    async def end_request(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsResult, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del ctx, stream, err, handler_state


async def make_standard_analytics_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CustomEndpointConfig,
) -> StandardAnalyticsSink:
    """Construct StandardAnalyticsSink asynchronously while the graph is initialized."""
    del ctx, config, environment
    return StandardAnalyticsSink()
