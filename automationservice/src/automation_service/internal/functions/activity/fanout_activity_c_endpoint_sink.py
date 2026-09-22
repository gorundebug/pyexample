"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class FanoutActivityCEndpointSink:
    """Implement FanoutActivityCEndpointSink."""


async def make_fanout_activity_c_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> FanoutActivityCEndpointSink:
    """Construct FanoutActivityCEndpointSink for the configured service graph."""
    del ctx, environment
    return FanoutActivityCEndpointSink()
