"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.endpoint_types import CronEndpointConfig
from pyservicelib_gorundebug.runtime.schedule import ScheduleTrigger
from pyservicelib_gorundebug.runtime.common import Collect


class LocalSchedule:
    """Implement LocalSchedule."""

    async def on_trigger(
        self,
        trigger: ScheduleTrigger,
        out: Collect[ScheduleTrigger],
    ) -> None:
        await out.out(trigger)


def make_local_schedule(
    ctx: Context,
    environment: ServiceEnvironment,
    config: CronEndpointConfig,
) -> LocalSchedule:
    """Construct LocalSchedule for the configured service graph."""
    del ctx, config, environment
    return LocalSchedule()
