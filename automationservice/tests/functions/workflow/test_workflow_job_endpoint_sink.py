"""User-owned tests for WorkflowJobEndpointSink."""

from automation_service.internal.functions.workflow.workflow_job_endpoint_sink import WorkflowJobEndpointSink


def test_workflow_job_endpoint_sink_contract_surface() -> None:
    function = WorkflowJobEndpointSink()