"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ObserveFanoutActivityB:
    """Observe the typed result returned by the Activity B fan-out branch."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out(value)


async def make_observe_fanout_activity_b(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ObserveFanoutActivityB:
    """Construct ObserveFanoutActivityB for the configured service graph."""
    del ctx, config, environment
    return ObserveFanoutActivityB()
