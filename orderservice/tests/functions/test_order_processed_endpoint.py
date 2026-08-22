"""User-owned tests for OrderProcessedEndpoint."""

from order_service.internal.functions.order_processed_endpoint import OrderProcessedEndpoint


def test_order_processed_contract_surface() -> None:
    function = OrderProcessedEndpoint()
    assert callable(function.get_stream_id)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
