"""User-owned tests for MultiJoinAnalyticsEvents."""

from analytics_service.internal.functions.multijoinanalytics.multi_join_analytics_events import MultiJoinAnalyticsEvents


def test_multi_join_analytics_events_contract_surface() -> None:
    function = MultiJoinAnalyticsEvents()
    assert callable(function.multi_join)