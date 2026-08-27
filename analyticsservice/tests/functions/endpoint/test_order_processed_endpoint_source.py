"""User-owned tests for OrderProcessedEndpointSource."""

from analytics_service.internal.functions.endpoint.order_processed_endpoint_source import OrderProcessedEndpointSource


def test_order_processed_contract_surface() -> None:
    function = OrderProcessedEndpointSource()
    assert callable(function.concurrency)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)
