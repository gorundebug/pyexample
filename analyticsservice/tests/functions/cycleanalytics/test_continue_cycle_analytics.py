"""User-owned tests for ContinueCycleAnalytics."""

from analytics_service.internal.functions.cycleanalytics.continue_cycle_analytics import ContinueCycleAnalytics


def test_continue_cycle_analytics_contract_surface() -> None:
    function = ContinueCycleAnalytics()
    assert callable(function.filter)