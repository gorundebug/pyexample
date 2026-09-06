"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import CustomEndpointConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from pyservicelib_gorundebug.datasource.localsource.custom import ResultContext
from pyservicelib_gorundebug.runtime.common import Consume, StreamContext


class AnalyticsShipmentsSource:
    """Produce a deterministic shipment analytics event for the canonical multi-way join example."""

    async def start(
        self,
        ctx: Context,
        consumer: Consume[AnalyticsEvent],
    ) -> None:
        del ctx
        await consumer.consume(AnalyticsEvent(key="high-value", value=30, kind="shipment"))
        await consumer.consume(AnalyticsEvent(key="standard", value=3, kind="shipment"))

    async def stop(self, ctx: Context) -> None:
        del ctx

    def concurrency(
        self,
        sc: StreamContext[AnalyticsEvent, AnalyticsEvent, Exception],
    ) -> int:
        del sc
        return 0

    async def begin_request(
        self,
        ctx: Context,
        sc: StreamContext[AnalyticsEvent, AnalyticsEvent, Exception],
    ) -> tuple[Context, None]:
        del sc
        return ctx, None

    async def consume_message(
        self,
        ctx: Context,
        sc: StreamContext[AnalyticsEvent, AnalyticsEvent, Exception],
        handler_state: None,
        value: AnalyticsEvent,
        result_ctx: ResultContext[None, AnalyticsEvent, AnalyticsEvent, Exception],
    ) -> None:
        del handler_state
        await sc.collect(value)
        result_ctx.done()

    def get_message_id(
        self,
        ctx: Context,
        sc: StreamContext[AnalyticsEvent, AnalyticsEvent, Exception],
        handler_state: None,
        value: AnalyticsEvent,
    ) -> str:
        del ctx, sc, handler_state, value
        return ""

    async def end_request(
        self,
        ctx: Context,
        sc: StreamContext[AnalyticsEvent, AnalyticsEvent, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del ctx, sc, err, handler_state


async def make_analytics_shipments_source(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CustomEndpointConfig,
) -> AnalyticsShipmentsSource:
    """Construct AnalyticsShipmentsSource asynchronously while the graph is initialized."""
    del ctx, config, environment
    return AnalyticsShipmentsSource()
