"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class WorkflowJobEndpointSink:
    """Implement WorkflowJobEndpointSink."""


async def make_workflow_job_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> WorkflowJobEndpointSink:
    """Construct WorkflowJobEndpointSink for the configured service graph."""
    del ctx, environment
    return WorkflowJobEndpointSink()
