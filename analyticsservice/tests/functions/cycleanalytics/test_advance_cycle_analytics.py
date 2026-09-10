"""User-owned tests for AdvanceCycleAnalytics."""

from analytics_service.internal.functions.cycleanalytics.advance_cycle_analytics import AdvanceCycleAnalytics


def test_advance_cycle_analytics_contract_surface() -> None:
    function = AdvanceCycleAnalytics()
    assert callable(function.map)