"""User-owned tests for ProcessDurableJob."""

import asyncio

from automation_service.internal.functions.process_durable_job import ProcessDurableJob


def test_process_durable_job_returns_a_stable_result() -> None:
    function = ProcessDurableJob()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    asyncio.run(function.map(None, "job-42", Collector()))  # type: ignore[arg-type]

    assert collected == ["processed:job-42"]
