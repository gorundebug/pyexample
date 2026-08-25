"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from pyservicelib_gorundebug.runtime import durable_call_heartbeat


class ProcessActivityJob:
    """Record Activity progress with DurableCallHeartbeat and return the processed job result."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        durable_call_heartbeat(f"processing:{value}")
        await out.out(f"activity:processed:{value}")


def make_process_activity_job(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessActivityJob:
    """Construct ProcessActivityJob for the configured service graph."""
    del ctx, config, environment
    return ProcessActivityJob()
