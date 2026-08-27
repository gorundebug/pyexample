"""User-owned tests for TemporalActivityScheduleSource."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.activity.temporal_activity_schedule_source import (
    TemporalActivityScheduleSource,
)
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_temporal_activity_schedule_converts_trigger() -> None:
    function = TemporalActivityScheduleSource()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 25, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-1", "activity-schedule", now, now, ScheduleBackend.TEMPORAL)
    asyncio.run(function.on_trigger(trigger, Collector()))  # type: ignore[arg-type]
    assert collected == ["scheduled-activity:activity-schedule:trigger-1"]
