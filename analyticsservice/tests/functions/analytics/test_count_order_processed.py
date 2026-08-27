"""User-owned tests for CountOrderProcessed."""

from analytics_service.internal.functions.analytics.count_order_processed import CountOrderProcessed


def test_count_order_processed_contract_surface() -> None:
    function = CountOrderProcessed()
    assert callable(function.process)