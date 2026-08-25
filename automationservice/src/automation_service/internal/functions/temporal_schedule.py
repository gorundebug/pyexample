"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
from pyservicelib_gorundebug.runtime.schedule import ScheduleTrigger
from pyservicelib_gorundebug.runtime.common import Collect


class TemporalSchedule:
    """Create a job message identifying the durable scheduled firing."""

    async def on_trigger(
        self,
        trigger: ScheduleTrigger,
        out: Collect[str],
    ) -> None:
        await out.out(f"temporal:{trigger.schedule_id}:{trigger.trigger_id}")


def make_temporal_schedule(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> TemporalSchedule:
    """Construct TemporalSchedule for the configured service graph."""
    del ctx, config, environment
    return TemporalSchedule()
