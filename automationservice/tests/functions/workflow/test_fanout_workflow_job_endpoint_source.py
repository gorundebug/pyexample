"""User-owned tests for FanoutWorkflowJobEndpointSource."""

from automation_service.internal.functions.workflow.fanout_workflow_job_endpoint_source import FanoutWorkflowJobEndpointSource


def test_fanout_workflow_job_endpoint_source_contract_surface() -> None:
    function = FanoutWorkflowJobEndpointSource()
    assert callable(function.begin_request)
    assert callable(function.consume_message)
    assert callable(function.end_request)
