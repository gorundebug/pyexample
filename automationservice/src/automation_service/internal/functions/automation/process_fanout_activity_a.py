"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ProcessFanoutActivityA:
    """Return Activity A's typed result before the Workflow Split."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out("fanout:a:" + value)


async def make_process_fanout_activity_a(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessFanoutActivityA:
    """Construct ProcessFanoutActivityA for the configured service graph."""
    del ctx, config, environment
    return ProcessFanoutActivityA()
