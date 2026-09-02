"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
class FanoutActivityCEndpointSink:
    """Implement FanoutActivityCEndpointSink."""


async def make_fanout_activity_c_endpoint_sink(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> FanoutActivityCEndpointSink:
    """Construct FanoutActivityCEndpointSink for the configured service graph."""
    del ctx, config, environment
    return FanoutActivityCEndpointSink()
