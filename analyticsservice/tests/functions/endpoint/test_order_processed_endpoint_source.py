"""User-owned tests for OrderProcessedEndpointSource."""

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from analytics_service.internal.functions.endpoint.order_processed_endpoint_source import OrderProcessedEndpointSource


def test_order_processed_contract_surface() -> None:
    function = OrderProcessedEndpointSource()
    assert callable(function.concurrency)
    assert callable(function.on_error)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)


@pytest.mark.asyncio
async def test_transport_error_is_forwarded_without_message_processing() -> None:
    handler = OrderProcessedEndpointSource()
    error = RuntimeError("broker unavailable")
    stream = SimpleNamespace(error_collect=AsyncMock())
    await handler.on_error(stream, error)
    stream.error_collect.assert_awaited_once_with(error)
