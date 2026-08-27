"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ProcessSequentialActivityB:
    """Return sequential Activity B's typed result to its Temporal sink."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out("sequential:b:" + value)


def make_process_sequential_activity_b(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessSequentialActivityB:
    """Construct ProcessSequentialActivityB for the configured service graph."""
    del ctx, config, environment
    return ProcessSequentialActivityB()
