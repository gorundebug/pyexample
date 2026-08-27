"""User-owned tests for ProcessScheduledActivity."""

from automation_service.internal.functions.automation.process_scheduled_activity import (
    ProcessScheduledActivity,
)


def test_process_scheduled_activity_contract_surface() -> None:
    function = ProcessScheduledActivity()
    assert callable(function.map)
