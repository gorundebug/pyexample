"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ProcessSequentialActivityA:
    """Return sequential Activity A's typed result to its Temporal sink."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out("sequential:a:" + value)


async def make_process_sequential_activity_a(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessSequentialActivityA:
    """Construct ProcessSequentialActivityA for the configured service graph."""
    del ctx, config, environment
    return ProcessSequentialActivityA()
