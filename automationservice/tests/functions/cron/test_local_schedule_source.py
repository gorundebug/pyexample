"""User-owned tests for LocalScheduleSource."""

import asyncio
from datetime import datetime, timezone

from automation_service.internal.functions.cron.local_schedule_source import LocalScheduleSource
from pyservicelib_gorundebug.runtime.schedule import ScheduleBackend, ScheduleTrigger


def test_local_schedule_converts_the_trigger_to_the_input_value() -> None:
    function = LocalScheduleSource()
    collected: list[str] = []

    class Collector:
        async def out(self, value: str) -> None:
            collected.append(value)

    now = datetime(2026, 8, 24, tzinfo=timezone.utc)
    trigger = ScheduleTrigger("trigger-1", "local-cleanup", now, now, ScheduleBackend.LOCAL)
    asyncio.run(function.on_trigger(trigger, Collector()))  # type: ignore[arg-type]

    assert collected == ["local:local-cleanup:trigger-1"]
