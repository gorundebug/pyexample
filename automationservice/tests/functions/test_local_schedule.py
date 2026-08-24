"""User-owned tests for LocalSchedule."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.local_schedule import LocalSchedule
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_local_schedule_emits_the_trigger() -> None:
    function = LocalSchedule()
    collected: list[ScheduleTrigger] = []

    class Collector:
        async def out(self, value: ScheduleTrigger) -> None:
            collected.append(value)

    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-1", "local-cleanup", now, now, ScheduleBackend.LOCAL)
    asyncio.run(function.on_trigger(trigger, Collector()))  # type: ignore[arg-type]

    assert collected == [trigger]
