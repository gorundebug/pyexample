# Task 31/36: `LocalScheduleSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `schedule-source` |
| File | `automationservice/src/automation_service/internal/functions/cron/local_schedule_source.py` |
| Test | `automationservice/tests/functions/test_cron/local_schedule_source.py` |
| Service | `Automation Service` |


## Behaviour

Create a job message identifying the local scheduled firing.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/cron/local_schedule_source.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_cron/local_schedule_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task31.md — LocalScheduleSource — Python — done`