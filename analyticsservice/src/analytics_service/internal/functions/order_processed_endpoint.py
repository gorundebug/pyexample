"""User-owned function implementation. The generator never overwrites this file."""

from pyservicelib_gorundebug.runtime.config.endpoint_types import KafkaEndpointConfig
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment
import json
from datetime import datetime

from model.models.order_processed import OrderProcessed
from pyservicelib_gorundebug.datasource.kafka.aiokafkads import (
    ConsumerMessage,
    ResultContext,
)
from pyservicelib_gorundebug.runtime.common import StreamContext


class OrderProcessedEndpoint:
    """Decode each OrderProcessed event and pass it to the analytics pipeline.
    Mark the Kafka message processed only after the pipeline has handled it successfully."""

    def concurrency(
        self,
        sc: StreamContext[OrderProcessed, OrderProcessed, Exception],
    ) -> int:
        del sc
        return 0

    async def begin_request(
        self,
        sc: StreamContext[OrderProcessed, OrderProcessed, Exception],
    ) -> None:
        del sc
        return None

    async def consume_message(
        self,
        sc: StreamContext[OrderProcessed, OrderProcessed, Exception],
        handler_state: None,
        message: ConsumerMessage,
        result_ctx: ResultContext[None, OrderProcessed, OrderProcessed, Exception],
    ) -> None:
        payload = json.loads((message.value or b"").decode())
        value = OrderProcessed(
            order_id=payload["order_id"],
            status=payload["status"],
            processed_at=datetime.fromisoformat(payload["processed_at"]),
            total_items=int(payload["total_items"]),
            confirmed_items=int(payload["confirmed_items"]),
            failure_reason=payload.get("failure_reason", ""),
        )

        def on_result(
            sc: StreamContext[OrderProcessed, OrderProcessed, Exception],
            handler_state: None,
            value: OrderProcessed,
        ) -> bool:
            del sc, handler_state, value

            message.mark_message("processed")
            result_ctx.done()
            return True

        result_ctx.set_result_callback(value.order_id, on_result)
        await sc.collect(value)

    def get_message_id(
        self,
        sc: StreamContext[OrderProcessed, OrderProcessed, Exception],
        handler_state: None,
        value: OrderProcessed,
    ) -> str:
        del sc, handler_state
        return value.order_id

    async def end_request(
        self,
        sc: StreamContext[OrderProcessed, OrderProcessed, Exception],
        err: Exception | None,
        handler_state: None,
    ) -> None:
        del sc, err, handler_state


def make_order_processed_endpoint(
    ctx: Context, environment: ServiceEnvironment, config: KafkaEndpointConfig
) -> OrderProcessedEndpoint:
    del ctx, environment, config
    return OrderProcessedEndpoint()
