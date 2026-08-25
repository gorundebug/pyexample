"""User-owned tests for ProcessActivityJob."""

import asyncio

from automation_service.internal.functions.process_activity_job import ProcessActivityJob
from pyservicelib_gorundebug.runtime.durable_context import (
    DurableCallContext,
    run_durable_call_activity,
)


def test_process_activity_job_records_progress_and_returns_result() -> None:
    function = ProcessActivityJob()
    collected: list[str] = []
    heartbeats: list[object] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    async def run() -> None:
        durable = DurableCallContext("activity-1", heartbeat=heartbeats.append)
        await run_durable_call_activity(
            durable,
            lambda: function.map(None, "job-1", Collector()),  # type: ignore[arg-type]
        )

    asyncio.run(run())
    assert heartbeats == ["processing:job-1"]
    assert collected == ["activity:processed:job-1"]
