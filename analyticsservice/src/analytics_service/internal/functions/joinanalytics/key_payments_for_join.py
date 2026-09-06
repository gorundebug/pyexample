"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from pyservicelib_gorundebug.runtime.config.stream_types import KeyByStreamConfig
from analytics_service.models.analytics_event import AnalyticsEvent
from pyservicelib_gorundebug.runtime.common import Collect, Stream
from pyservicelib_gorundebug.runtime.datastruct import KeyValue


class KeyPaymentsForJoin:
    """Key the payment analytics event by correlation key."""

    async def key_by(
        self,
        stream: Stream,
        value: AnalyticsEvent,
        out: Collect[KeyValue[str, AnalyticsEvent]],
    ) -> None:
        del stream
        await out.out(KeyValue(value.key, value))


async def make_key_payments_for_join(
    ctx: Context,
    environment: ServiceEnvironment,
    config: KeyByStreamConfig,
) -> KeyPaymentsForJoin:
    """Construct KeyPaymentsForJoin asynchronously while the graph is initialized."""
    del ctx, config, environment
    return KeyPaymentsForJoin()
