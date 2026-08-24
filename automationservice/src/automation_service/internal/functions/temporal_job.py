"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import MapStreamConfig
from pyservicelib_gorundebug.runtime.schedule import ScheduleTrigger
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class TemporalJob:
    """Create a job message identifying the durable scheduled firing."""

    async def map(
        self,
        stream: Stream,
        value: ScheduleTrigger,
        out: Collect[str],
    ) -> None:
        del stream
        await out.out(f"temporal:{value.schedule_id}:{value.trigger_id}")


def make_temporal_job(
    ctx: Context,
    environment: ServiceEnvironment,
    config: MapStreamConfig,
) -> TemporalJob:
    """Construct TemporalJob for the configured service graph."""
    del ctx, config, environment
    return TemporalJob()
