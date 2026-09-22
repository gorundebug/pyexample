"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class FanoutWorkflowJobEndpointSink:
    """Implement FanoutWorkflowJobEndpointSink."""


async def make_fanout_workflow_job_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> FanoutWorkflowJobEndpointSink:
    """Construct FanoutWorkflowJobEndpointSink for the configured service graph."""
    del ctx, environment
    return FanoutWorkflowJobEndpointSink()
