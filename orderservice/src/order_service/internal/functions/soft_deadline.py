"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.stream_types import DelayStreamConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from datetime import datetime, timedelta, timezone

from order_service.models.order import Order
from pyservicelib_gorundebug.runtime.context.request import request_deadline
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class SoftDeadline:
    """Trigger the timeout branch shortly before the request deadline, leaving the configured duration to assemble a response.
    When no request deadline exists, use the configured duration itself. Never wait past an existing deadline."""

    async def duration(self, stream: Stream, value: Order) -> timedelta:
        del value
        duration_ms = getattr(stream.config, "duration", 0) or 0
        margin = timedelta(milliseconds=duration_ms)
        deadline = request_deadline.get()
        if deadline is None:
            return margin
        now = datetime.now(timezone.utc if deadline.tzinfo is not None else None)
        remaining = deadline - now - margin
        return max(remaining, timedelta())

    async def delay_error(
        self,
        stream: Stream,
        value: Order,
        error: Exception,
        out: Collect[Order],
    ) -> None:
        del stream, value, error, out


def make_soft_deadline(
    ctx: Context, environment: ServiceEnvironment, config: DelayStreamConfig
) -> SoftDeadline:
    del ctx, environment, config
    return SoftDeadline()
