"""User-owned tests for TemporalJob."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.temporal_job import TemporalJob
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_temporal_job_formats_the_scheduled_trigger() -> None:
    function = TemporalJob()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-2", "durable-report", now, now, ScheduleBackend.TEMPORAL)
    asyncio.run(function.map(None, trigger, Collector()))  # type: ignore[arg-type]

    assert collected == ["temporal:durable-report:trigger-2"]
