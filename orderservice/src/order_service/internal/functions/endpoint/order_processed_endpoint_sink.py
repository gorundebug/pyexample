"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.endpoint_types import KafkaEndpointConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
from dataclasses import asdict
from datetime import datetime
import json

from typing import cast

from model.models.order_processed import OrderProcessed
from pyservicelib_gorundebug.datasink.kafka.aiokafkads import SinkMessage
from pyservicelib_gorundebug.runtime.common import Stream


class OrderProcessedEndpointSink:
    """Publish the OrderProcessed event produced by MapToOrderProcessed."""

    def get_stream_id(self, value: OrderProcessed) -> str:
        return value.order_id

    def begin_request(self, stream: Stream) -> None:
        del stream
        return None

    async def consume_message(
        self,
        stream: Stream,
        handler_state: None,
        value: OrderProcessed,
        message: SinkMessage[Exception],
    ) -> None:
        message.key = value.order_id.encode()
        message.value = json.dumps(
            asdict(value),
            separators=(",", ":"),
            default=_json_default,
        ).encode()
        message.send(lambda _partition, _offset, err: cast(Exception, err))

    async def end_request(
        self,
        stream: Stream,
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del stream, err, handler_state


async def make_order_processed_endpoint_sink(
    ctx: Context, environment: ServiceEnvironment, config: KafkaEndpointConfig
) -> OrderProcessedEndpointSink:
    del ctx, environment, config
    return OrderProcessedEndpointSink()


def _json_default(value: object) -> str:
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError(f"cannot serialize {type(value).__name__} to JSON")
