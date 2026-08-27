"""User-owned tests for WorkflowJobEndpointSource."""

from automation_service.internal.functions.workflow.workflow_job_endpoint_source import WorkflowJobEndpointSource


def test_workflow_job_endpoint_source_contract_surface() -> None:
    function = WorkflowJobEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
