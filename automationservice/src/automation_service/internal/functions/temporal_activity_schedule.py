"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import TemporalEndpointConfig
from pyservicelib_gorundebug.runtime.schedule import ScheduleTrigger
from pyservicelib_gorundebug.runtime.common import Collect


class TemporalActivitySchedule:
    """Create an Activity job message identifying the durable scheduled firing."""

    async def on_trigger(
        self,
        trigger: ScheduleTrigger,
        out: Collect[str],
    ) -> None:
        await out.out(f"scheduled-activity:{trigger.schedule_id}:{trigger.trigger_id}")


def make_temporal_activity_schedule(
    ctx: Context,
    environment: ServiceEnvironment,
    config: TemporalEndpointConfig,
) -> TemporalActivitySchedule:
    """Construct TemporalActivitySchedule for the configured service graph."""
    del ctx, config, environment
    return TemporalActivitySchedule()
