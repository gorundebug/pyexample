"""User-owned tests for AnalyticsOrdersSource."""

from analytics_service.internal.functions.endpoint.analytics_orders_source import AnalyticsOrdersSource


def test_analytics_orders_source_contract_surface() -> None:
    function = AnalyticsOrdersSource()
    assert callable(function.concurrency)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)