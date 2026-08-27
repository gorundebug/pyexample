"""User-owned tests for ProcessScheduledWorkflow."""

from automation_service.internal.functions.automation.process_scheduled_workflow import (
    ProcessScheduledWorkflow,
)


def test_process_scheduled_workflow_contract_surface() -> None:
    function = ProcessScheduledWorkflow()
    assert callable(function.map)
