"""User-owned tests for AnalyticsPaymentsSource."""

from analytics_service.internal.functions.endpoint.analytics_payments_source import AnalyticsPaymentsSource


def test_analytics_payments_source_contract_surface() -> None:
    function = AnalyticsPaymentsSource()
    assert callable(function.concurrency)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)