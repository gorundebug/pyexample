"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import CustomEndpointConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from pyservicelib_gorundebug.runtime.common import Collect, TypedSinkStream


class CycleAnalyticsResultSink:
    """Validate the terminal event emitted after three passes through the feedback cycle."""

    def get_stream_id(self, ctx: Context, value: AnalyticsEvent) -> str:
        del ctx, value
        return ""

    async def begin_request(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsEvent, Exception],
    ) -> tuple[Context, None]:
        del stream
        return ctx, None

    async def consume_message(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsEvent, Exception],
        handler_state: None,
        value: AnalyticsEvent,
        result_stream: Collect[Exception],
    ) -> None:
        del ctx, stream, handler_state, result_stream
        if value != AnalyticsEvent(key="cycle", value=3, kind="cycle"):
            raise ValueError(f"unexpected cycle analytics result: {value!r}")

    async def end_request(
        self,
        ctx: Context,
        stream: TypedSinkStream[AnalyticsEvent, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del ctx, stream, err, handler_state


async def make_cycle_analytics_result_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CustomEndpointConfig,
) -> CycleAnalyticsResultSink:
    """Construct CycleAnalyticsResultSink asynchronously while the graph is initialized."""
    del ctx, config, environment
    return CycleAnalyticsResultSink()
