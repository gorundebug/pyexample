"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
class FanoutWorkflowJobEndpointSink:
    """Implement FanoutWorkflowJobEndpointSink."""


def make_fanout_workflow_job_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> FanoutWorkflowJobEndpointSink:
    """Construct FanoutWorkflowJobEndpointSink for the configured service graph."""
    del ctx, config, environment
    return FanoutWorkflowJobEndpointSink()