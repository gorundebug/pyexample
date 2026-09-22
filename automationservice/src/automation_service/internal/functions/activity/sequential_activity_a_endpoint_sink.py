"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class SequentialActivityAEndpointSink:
    """Implement SequentialActivityAEndpointSink."""


async def make_sequential_activity_a_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> SequentialActivityAEndpointSink:
    """Construct SequentialActivityAEndpointSink for the configured service graph."""
    del ctx, environment
    return SequentialActivityAEndpointSink()
