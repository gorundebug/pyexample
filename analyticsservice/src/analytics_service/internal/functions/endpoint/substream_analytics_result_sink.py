"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from analytics_service.models.analytics_result import AnalyticsResult
from pyservicelib_gorundebug.runtime.common import Collect, TypedSinkStream
class SubstreamAnalyticsResultSink:
    """Validate and record the result returned by the service-local SubStream example."""

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
        expected = AnalyticsResult(key="substream", total=14, kind="substream")
        if value != expected:
            raise ValueError(f"unexpected substream analytics result: {value!r}")

    async def end_request(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsResult, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del ctx, stream, err, handler_state


async def make_substream_analytics_result_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> SubstreamAnalyticsResultSink:
    """Construct SubstreamAnalyticsResultSink asynchronously while the graph is initialized."""
    del ctx, environment
    return SubstreamAnalyticsResultSink()
