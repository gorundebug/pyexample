"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class ActivityJobEndpointSink:
    """Implement ActivityJobEndpointSink."""


async def make_activity_job_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> ActivityJobEndpointSink:
    """Construct ActivityJobEndpointSink for the configured service graph."""
    del ctx, environment
    return ActivityJobEndpointSink()
