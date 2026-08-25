"""User-owned tests for TemporalSchedule."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.temporal_schedule import TemporalSchedule
from pyservicelib_gorundebug.runtime.durable_context import (
    DurableCallContext,
    run_durable_call_activity,
)
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_temporal_schedule_converts_the_trigger_to_the_input_value() -> None:
    function = TemporalSchedule()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-1", "temporal-cleanup", now, now, ScheduleBackend.TEMPORAL)

    async def run() -> None:
        durable = DurableCallContext("test")
        await asyncio.wait_for(
            run_durable_call_activity(
                durable,
                lambda: function.on_trigger(trigger, Collector()),  # type: ignore[arg-type]
            ),
            timeout=1,
        )

    asyncio.run(run())

    assert collected == ["temporal:temporal-cleanup:trigger-1"]
