"""User-owned tests for WorkflowPause."""

from automation_service.internal.functions.workflow_pause import WorkflowPause


def test_workflow_pause_contract_surface() -> None:
    function = WorkflowPause()
    assert callable(function.duration)
    assert callable(function.delay_error)
