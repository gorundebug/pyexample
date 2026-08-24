"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.schedule import ScheduleTrigger
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class LocalJob:
    """Create a job message identifying the local scheduled firing."""

    async def map(
        self,
        stream: Stream,
        value: ScheduleTrigger,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out(f"local:{value.schedule_id}:{value.trigger_id}")


def make_local_job(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> LocalJob:
    """Construct LocalJob for the configured service graph."""
    del ctx, config, environment
    return LocalJob()
