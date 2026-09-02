"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from pyservicelib_gorundebug.runtime import durable_call_heartbeat


class ProcessScheduledActivity:
    """Return the visible result of one scheduled Activity execution."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        durable_call_heartbeat(f"processing:{value}")
        await out.out(f"activity:processed:{value}")


async def make_process_scheduled_activity(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessScheduledActivity:
    """Construct ProcessScheduledActivity for the configured service graph."""
    del ctx, config, environment
    return ProcessScheduledActivity()
