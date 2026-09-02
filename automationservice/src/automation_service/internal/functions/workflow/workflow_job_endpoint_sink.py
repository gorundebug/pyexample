"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
class WorkflowJobEndpointSink:
    """Implement WorkflowJobEndpointSink."""


async def make_workflow_job_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> WorkflowJobEndpointSink:
    """Construct WorkflowJobEndpointSink for the configured service graph."""
    del ctx, config, environment
    return WorkflowJobEndpointSink()
