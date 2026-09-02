"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
from pyservicelib_gorundebug.runtime.common import StreamContext


class FanoutWorkflowJobEndpointSource:
    """Implement FanoutWorkflowJobEndpointSource."""

    async def begin_request(
        self, ctx: Context, sc: StreamContext[str, str, Exception]
    ) -> tuple[Context, None]:
        del sc
        return ctx, None

    async def consume_message(
        self, ctx: Context, sc: StreamContext[str, str, Exception], handler_state: None, value: str
    ) -> None:
        del ctx, handler_state
        await sc.collect(value)

    async def end_request(
        self,
        ctx: Context,
        sc: StreamContext[str, str, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del ctx, sc, err, handler_state


async def make_fanout_workflow_job_endpoint_source(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> FanoutWorkflowJobEndpointSource:
    """Construct FanoutWorkflowJobEndpointSource for the configured service graph."""
    del ctx, config, environment
    return FanoutWorkflowJobEndpointSource()
