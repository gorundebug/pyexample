"""User-owned tests for TemporalSchedule."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.temporal_schedule import TemporalSchedule
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_temporal_schedule_emits_the_trigger() -> None:
    function = TemporalSchedule()
    collected: list[ScheduleTrigger] = []

    class Collector:
        async def out(self, value: ScheduleTrigger) -> None:
            collected.append(value)

    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    trigger = ScheduleTrigger(
        "trigger-1", "temporal-cleanup", now, now, ScheduleBackend.TEMPORAL
    )
    asyncio.run(function.on_trigger(trigger, Collector()))  # type: ignore[arg-type]

    assert collected == [trigger]
