"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.stream_types import ProcessStreamConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from model.models.order_processed import OrderProcessed
from pyservicelib_gorundebug.runtime.common import Collect, Stream


class CountOrderProcessed:
    """Count successful and unsuccessful orders independently, then return the event unchanged."""

    async def process(
        self,
        stream: Stream,
        value: OrderProcessed,
        out: Collect[OrderProcessed],
        err_out: Collect[Exception],
    ) -> None:
        del stream, err_out
        if value.status == "CONFIRMED":
            self.successful += 1
        else:
            self.unsuccessful += 1
        await out.out(value)

    def __init__(self) -> None:
        self.successful = 0
        self.unsuccessful = 0


async def make_count_order_processed(
    ctx: Context, environment: ServiceEnvironment, config: ProcessStreamConfig
) -> CountOrderProcessed:
    del ctx, environment, config
    return CountOrderProcessed()
