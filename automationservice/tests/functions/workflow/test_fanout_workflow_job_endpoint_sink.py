"""User-owned tests for FanoutWorkflowJobEndpointSink."""

from automation_service.internal.functions.workflow.fanout_workflow_job_endpoint_sink import FanoutWorkflowJobEndpointSink


def test_fanout_workflow_job_endpoint_sink_contract_surface() -> None:
    function = FanoutWorkflowJobEndpointSink()