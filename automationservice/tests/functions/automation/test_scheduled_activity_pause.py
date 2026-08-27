"""User-owned tests for ScheduledActivityPause."""

from automation_service.internal.functions.automation.scheduled_activity_pause import ScheduledActivityPause


def test_scheduled_activity_pause_contract_surface() -> None:
    function = ScheduledActivityPause()
    assert callable(function.duration)
    assert callable(function.delay_error)
