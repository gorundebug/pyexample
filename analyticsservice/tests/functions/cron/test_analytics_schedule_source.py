"""User-owned tests for AnalyticsScheduleSource."""

from analytics_service.internal.functions.cron.analytics_schedule_source import AnalyticsScheduleSource


def test_analytics_schedule_source_contract_surface() -> None:
    function = AnalyticsScheduleSource()
    assert callable(function.on_trigger)