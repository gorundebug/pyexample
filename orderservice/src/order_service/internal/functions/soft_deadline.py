"""User-owned function implementation. The generator never overwrites this file."""
from datetime import datetime, timedelta, timezone

from order_service.models.order import Order
from pyservicelib_gorundebug.runtime.context.request import request_deadline
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class SoftDeadline:
    """Cast stream.GetConfig() to *runtimecfg.DelayStreamConfig and convert cfg.Duration (int, milliseconds) to time.Duration — this is the safety margin.
If ctx has no deadline (ctx.Deadline() ok==false), return the margin directly.
Otherwise compute time.Until(deadline) minus the margin: if the result is negative return 0, otherwise return it."""

    async def duration(self, stream: Stream, value: Order) -> timedelta:
        del value
        duration_ms = getattr(stream.config, "duration", 0) or 0
        margin = timedelta(milliseconds=duration_ms)
        deadline = request_deadline.get()
        if deadline is None:
            return margin
        now = datetime.now(
            timezone.utc if deadline.tzinfo is not None else None
        )
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
