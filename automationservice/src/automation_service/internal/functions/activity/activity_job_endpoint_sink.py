"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
class ActivityJobEndpointSink:
    """Implement ActivityJobEndpointSink."""


def make_activity_job_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> ActivityJobEndpointSink:
    """Construct ActivityJobEndpointSink for the configured service graph."""
    del ctx, config, environment
    return ActivityJobEndpointSink()