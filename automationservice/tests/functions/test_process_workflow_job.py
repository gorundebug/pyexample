"""User-owned tests for ProcessWorkflowJob."""

import asyncio
from datetime import timedelta

from automation_service.internal.functions.process_workflow_job import ProcessWorkflowJob
from pyservicelib_gorundebug.runtime.durable_context import (
    DurableCallContext,
    TemporalContinueAsNewRequest,
    run_durable_call_workflow,
)


def test_process_workflow_job_continues_once_and_returns_final_result() -> None:
    function = ProcessWorkflowJob()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    async def timer(_duration: timedelta) -> None:
        return None

    async def run() -> None:
        first = DurableCallContext("workflow-1", delay=timer, workflow=True)
        try:
            await run_durable_call_workflow(
                first,
                lambda: function.map(None, "job-1", Collector()),  # type: ignore[arg-type]
            )
        except TemporalContinueAsNewRequest as request:
            assert request.next_input == "continued:job-1"
        else:
            raise AssertionError("first run must Continue-As-New")

        second = DurableCallContext("workflow-2", delay=timer, workflow=True)
        await run_durable_call_workflow(
            second,
            lambda: function.map(None, "continued:job-1", Collector()),  # type: ignore[arg-type]
        )

    asyncio.run(run())
    assert collected == ["workflow:processed:job-1"]
