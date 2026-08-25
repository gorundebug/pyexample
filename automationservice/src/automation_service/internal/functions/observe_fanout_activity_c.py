"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ObserveFanoutActivityC:
    """Observe the typed result returned by the Activity C fan-out branch."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out(value)


def make_observe_fanout_activity_c(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ObserveFanoutActivityC:
    """Construct ObserveFanoutActivityC for the configured service graph."""
    del ctx, config, environment
    return ObserveFanoutActivityC()
