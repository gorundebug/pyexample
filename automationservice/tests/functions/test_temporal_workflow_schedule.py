"""User-owned tests for TemporalWorkflowSchedule."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.temporal_workflow_schedule import (
    TemporalWorkflowSchedule,
)
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_temporal_workflow_schedule_converts_trigger() -> None:
    function = TemporalWorkflowSchedule()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 25, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-2", "workflow-schedule", now, now, ScheduleBackend.TEMPORAL)
    asyncio.run(function.on_trigger(trigger, Collector()))  # type: ignore[arg-type]
    assert collected == ["scheduled-workflow:workflow-schedule:trigger-2"]
