"""User-owned tests for ObserveWorkflowResult."""

from automation_service.internal.functions.observe_workflow_result import ObserveWorkflowResult


def test_observe_workflow_result_contract_surface() -> None:
    function = ObserveWorkflowResult()
    assert callable(function.map)
