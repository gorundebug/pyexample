"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
class FanoutActivityBEndpointSink:
    """Implement FanoutActivityBEndpointSink."""


async def make_fanout_activity_b_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> FanoutActivityBEndpointSink:
    """Construct FanoutActivityBEndpointSink for the configured service graph."""
    del ctx, config, environment
    return FanoutActivityBEndpointSink()
