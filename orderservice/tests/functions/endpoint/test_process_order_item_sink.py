"""User-owned tests for ProcessOrderItemSink."""

import pytest

from order_service.internal.functions.endpoint.process_order_item_sink import ProcessOrderItemSink


def test_process_order_item_sink_contract_surface() -> None:
    function = ProcessOrderItemSink()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.handle_response)
    assert callable(function.end_request)


@pytest.mark.asyncio
async def test_end_request_publishes_processing_error() -> None:
    class Stream:
        def __init__(self) -> None:
            self.values = []

        async def collect(self, value) -> None:
            self.values.append(value)

    function = ProcessOrderItemSink()
    stream = Stream()
    state = ProcessOrderItemSink.State(
        order_id="order-1",
        item_id="item-1",
        sku="SKU-001",
        requested_qty=3,
        unit_price=12.5,
    )

    await function.end_request(stream, RuntimeError("inventory unavailable"), state)  # type: ignore[arg-type]

    assert len(stream.values) == 1
    result = stream.values[0]
    assert result.status == "PROCESSING_ERROR"
    assert result.error == "inventory unavailable"
    assert result.reserved is False
    assert result.available_qty == 0
