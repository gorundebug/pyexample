"""User-owned tests for AnalyticsShipmentsSource."""

from analytics_service.internal.functions.endpoint.analytics_shipments_source import AnalyticsShipmentsSource


def test_analytics_shipments_source_contract_surface() -> None:
    function = AnalyticsShipmentsSource()
    assert callable(function.concurrency)
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.get_message_id)
    assert callable(function.end_request)