"""Exercise generated initializer barriers without running business implementations."""

import asyncio
from collections.abc import Awaitable, Callable
from typing import Any

import pytest
from pyservicelib_gorundebug.runtime.context.context import Context
from pyservicelib_gorundebug.runtime.environment import ServiceEnvironment

from automation_service.internal.app.service_generated import GeneratedService
from automation_service.internal.config import Config


GROUPS: list[list[str]] = [
    ["activity_job_endpoint_sink", "activity_job_endpoint_source", "fanout_activity_a_endpoint_sink", "fanout_activity_a_endpoint_source", "fanout_activity_b_endpoint_sink", "fanout_activity_b_endpoint_source", "fanout_activity_c_endpoint_sink", "fanout_activity_c_endpoint_source", "sequential_activity_a_endpoint_sink", "sequential_activity_a_endpoint_source", "sequential_activity_b_endpoint_sink", "sequential_activity_b_endpoint_source", "temporal_activity_schedule_source", "activity_pause", "observe_activity_result", "observe_fanout_activity_b", "observe_fanout_activity_c", "observe_workflow_result", "process_activity_job", "process_fanout_activity_a", "process_fanout_activity_b", "process_fanout_activity_c", "process_scheduled_activity", "process_scheduled_workflow", "process_sequential_activity_a", "process_sequential_activity_b", "process_workflow_job", "scheduled_activity_pause", "scheduled_workflow_pause", "workflow_pause", "local_schedule_source", "fanout_workflow_job_endpoint_sink", "fanout_workflow_job_endpoint_source", "temporal_workflow_schedule_source", "workflow_job_endpoint_sink", "workflow_job_endpoint_source", ],
]


def _service() -> GeneratedService:
    service = GeneratedService()
    config = Config.from_dict({})
    assert config is not None
    service.set_config(config)
    return service


@pytest.mark.asyncio
async def test_function_groups_start_all_members_before_advancing() -> None:
    service = _service()
    entered: list[set[str]] = [set() for _ in GROUPS]
    completed: list[set[str]] = [set() for _ in GROUPS]
    barriers = [asyncio.Event() for _ in GROUPS]
    instances: dict[str, object] = {}

    def maker(name: str, index: int) -> Callable[[Context, ServiceEnvironment], Awaitable[Any]]:
        async def create(_ctx: Context, _environment: ServiceEnvironment) -> Any:
            if index:
                assert completed[index - 1] == set(GROUPS[index - 1])
            assert name not in entered[index]
            entered[index].add(name)
            if entered[index] == set(GROUPS[index]):
                barriers[index].set()
            await barriers[index].wait()
            result = object()
            instances[name] = result
            completed[index].add(name)
            return result

        return create

    for index, names in enumerate(GROUPS):
        for name in names:
            setattr(service.makers, name, maker(name, index))
    await asyncio.wait_for(service.initialize_functions(Context()), timeout=10)
    assert completed == [set(names) for names in GROUPS]
    for name, instance in instances.items():
        assert getattr(service.functions, name) is instance


@pytest.mark.asyncio
async def test_failed_group_waits_for_members_and_stops_following_groups() -> None:
    if not GROUPS:
        return
    service = _service()
    entered: set[str] = set()
    completed: set[str] = set()
    all_started = asyncio.Event()
    failure = RuntimeError("initializer regression sentinel")
    first_name = GROUPS[0][0]

    def maker(name: str, index: int) -> Callable[[Context, ServiceEnvironment], Awaitable[Any]]:
        async def create(_ctx: Context, _environment: ServiceEnvironment) -> Any:
            assert index == 0, "a later group started after failure"
            entered.add(name)
            if entered == set(GROUPS[0]):
                all_started.set()
            if name == first_name:
                raise failure
            await all_started.wait()
            completed.add(name)
            return object()

        return create

    for index, names in enumerate(GROUPS):
        for name in names:
            setattr(service.makers, name, maker(name, index))
    with pytest.raises(RuntimeError) as raised:
        await asyncio.wait_for(service.initialize_functions(Context()), timeout=10)
    assert raised.value is failure
    assert entered == set(GROUPS[0])
    assert completed == set(GROUPS[0]) - {first_name}