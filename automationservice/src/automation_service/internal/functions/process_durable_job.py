"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from pyservicelib_gorundebug.runtime.durable_context import durable_call_success


class ProcessDurableJob:
    """Process one accepted automation job and return its result."""

    async def map(
        self,
        stream: Stream,
        value: str,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out(f"processed:{value}")
        durable_call_success()


def make_process_durable_job(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> ProcessDurableJob:
    """Construct ProcessDurableJob for the configured service graph."""
    del ctx, config, environment
    return ProcessDurableJob()
