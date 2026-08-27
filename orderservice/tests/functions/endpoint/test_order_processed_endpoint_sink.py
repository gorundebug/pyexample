"""User-owned tests for OrderProcessedEndpointSink."""

from order_service.internal.functions.endpoint.order_processed_endpoint_sink import OrderProcessedEndpointSink


def test_order_processed_contract_surface() -> None:
    function = OrderProcessedEndpointSink()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
