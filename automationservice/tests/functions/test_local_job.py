"""User-owned tests for LocalJob."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.local_job import LocalJob
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_local_job_formats_the_scheduled_trigger() -> None:
    function = LocalJob()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-1", "local-cleanup", now, now, ScheduleBackend.LOCAL)
    asyncio.run(function.map(None, trigger, Collector()))  # type: ignore[arg-type]

    assert collected == ["local:local-cleanup:trigger-1"]
