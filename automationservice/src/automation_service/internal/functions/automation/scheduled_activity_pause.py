"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import DelayStreamConfig
from datetime import timedelta
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class ScheduledActivityPause:
    """Apply the ordinary local Delay inside an Activity started by Temporal Schedule."""

    async def duration(self, stream: Stream, value: str) -> timedelta:
        del value
        duration_ms = getattr(stream.config, "duration", 0) or 0
        return timedelta(milliseconds=duration_ms)

    async def delay_error(
        self,
        stream: Stream,
        value: str,
        error: Exception,
        out: Collect[str],
    ) -> None:
        del stream, value, error, out


async def make_scheduled_activity_pause(
    ctx: Context,
    environment: ServiceEnvironment,
    config: DelayStreamConfig,
) -> ScheduledActivityPause:
    """Construct ScheduledActivityPause for the configured service graph."""
    del ctx, config, environment
    return ScheduledActivityPause()
