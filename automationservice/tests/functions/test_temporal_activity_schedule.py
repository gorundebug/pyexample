"""User-owned tests for TemporalActivitySchedule."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.temporal_activity_schedule import (
    TemporalActivitySchedule,
)
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_temporal_activity_schedule_converts_trigger() -> None:
    function = TemporalActivitySchedule()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 25, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-1", "activity-schedule", now, now, ScheduleBackend.TEMPORAL)
    asyncio.run(function.on_trigger(trigger, Collector()))  # type: ignore[arg-type]
    assert collected == ["scheduled-activity:activity-schedule:trigger-1"]
