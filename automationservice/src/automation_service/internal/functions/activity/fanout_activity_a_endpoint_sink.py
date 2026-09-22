"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class FanoutActivityAEndpointSink:
    """Implement FanoutActivityAEndpointSink."""


async def make_fanout_activity_a_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> FanoutActivityAEndpointSink:
    """Construct FanoutActivityAEndpointSink for the configured service graph."""
    del ctx, environment
    return FanoutActivityAEndpointSink()
