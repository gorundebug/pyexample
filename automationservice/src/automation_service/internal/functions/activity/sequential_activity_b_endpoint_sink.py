"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

class SequentialActivityBEndpointSink:
    """Implement SequentialActivityBEndpointSink."""


async def make_sequential_activity_b_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
) -> SequentialActivityBEndpointSink:
    """Construct SequentialActivityBEndpointSink for the configured service graph."""
    del ctx, environment
    return SequentialActivityBEndpointSink()
