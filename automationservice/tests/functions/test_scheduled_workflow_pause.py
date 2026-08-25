"""User-owned tests for ScheduledWorkflowPause."""

from automation_service.internal.functions.scheduled_workflow_pause import ScheduledWorkflowPause


def test_scheduled_workflow_pause_contract_surface() -> None:
    function = ScheduledWorkflowPause()
    assert callable(function.duration)
    assert callable(function.delay_error)
