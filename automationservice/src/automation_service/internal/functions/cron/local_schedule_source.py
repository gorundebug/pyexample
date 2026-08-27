"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import CronEndpointConfig
from pyservicelib_gorundebug.runtime.schedule import ScheduleTrigger
from pyservicelib_gorundebug.runtime.common import Collect


class LocalScheduleSource:
    """Create a job message identifying the local scheduled firing."""

    async def on_trigger(
        self,
        trigger: ScheduleTrigger,
        out: Collect[str],
    ) -> None:
        await out.out(f"local:{trigger.schedule_id}:{trigger.trigger_id}")


def make_local_schedule_source(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CronEndpointConfig,
) -> LocalScheduleSource:
    """Construct LocalScheduleSource for the configured service graph."""
    del ctx, config, environment
    return LocalScheduleSource()
