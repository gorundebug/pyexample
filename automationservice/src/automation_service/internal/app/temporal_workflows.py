"""User-owned maker customization for Temporal Workflow execution."""

from pyservicelib_gorundebug.runtime.context.context import Context

from .workflow_graph_generated import ServiceMakers


def custom_workflow_makers_init(
    context: Context,
    makers: ServiceMakers,
) -> None:
    """Override makers used only inside the Temporal Workflow sandbox."""

    del context, makers
    # makers.activity_pause = custom_activity_pause_maker
    # makers.local_schedule = custom_local_schedule_maker
    # makers.observe_activity_result = custom_observe_activity_result_maker
    # makers.observe_fanout_activity_b = custom_observe_fanout_activity_b_maker
    # makers.observe_fanout_activity_c = custom_observe_fanout_activity_c_maker
    # makers.observe_workflow_result = custom_observe_workflow_result_maker
    # makers.process_activity_job = custom_process_activity_job_maker
    # makers.process_fanout_activity_a = custom_process_fanout_activity_a_maker
    # makers.process_fanout_activity_b = custom_process_fanout_activity_b_maker
    # makers.process_fanout_activity_c = custom_process_fanout_activity_c_maker
    # makers.process_scheduled_activity = custom_process_scheduled_activity_maker
    # makers.process_scheduled_workflow = custom_process_scheduled_workflow_maker
    # makers.process_sequential_activity_a = custom_process_sequential_activity_a_maker
    # makers.process_sequential_activity_b = custom_process_sequential_activity_b_maker
    # makers.process_workflow_job = custom_process_workflow_job_maker
    # makers.scheduled_activity_pause = custom_scheduled_activity_pause_maker
    # makers.scheduled_workflow_pause = custom_scheduled_workflow_pause_maker
    # makers.temporal_activity_schedule = custom_temporal_activity_schedule_maker
    # makers.temporal_workflow_schedule = custom_temporal_workflow_schedule_maker
    # makers.workflow_pause = custom_workflow_pause_maker