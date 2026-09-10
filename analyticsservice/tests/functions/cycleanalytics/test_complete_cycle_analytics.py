"""User-owned tests for CompleteCycleAnalytics."""

from analytics_service.internal.functions.cycleanalytics.complete_cycle_analytics import CompleteCycleAnalytics


def test_complete_cycle_analytics_contract_surface() -> None:
    function = CompleteCycleAnalytics()
    assert callable(function.filter)