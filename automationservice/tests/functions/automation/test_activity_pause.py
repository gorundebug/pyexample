"""User-owned tests for ActivityPause."""

from automation_service.internal.functions.automation.activity_pause import ActivityPause


def test_activity_pause_contract_surface() -> None:
    function = ActivityPause()
    assert callable(function.duration)
    assert callable(function.delay_error)
