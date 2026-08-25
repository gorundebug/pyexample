"""User-owned tests for ProcessDurableJob."""

import asyncio

from automation_service.internal.functions.process_durable_job import ProcessDurableJob
from pyservicelib_gorundebug.runtime.durable_context import (
    DurableCallContext,
    run_durable_call_activity,
)


def test_process_durable_job_returns_a_stable_result() -> None:
    function = ProcessDurableJob()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    async def run() -> None:
        durable = DurableCallContext("test")
        await asyncio.wait_for(
            run_durable_call_activity(
                durable,
                lambda: function.map(None, "job-42", Collector()),  # type: ignore[arg-type]
            ),
            timeout=1,
        )

    asyncio.run(run())

    assert collected == ["processed:job-42"]
