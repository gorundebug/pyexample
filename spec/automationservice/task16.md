# Task 16/20: `ScheduledActivityPause`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `delay` |
| File | `automationservice/src/automation_service/internal/functions/scheduled_activity_pause.py` |
| Test | `automationservice/tests/functions/test_scheduled_activity_pause.py` |
| Service | `Automation Service` |


## Behaviour

Apply the ordinary local Delay inside an Activity started by Temporal Schedule.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/scheduled_activity_pause.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_scheduled_activity_pause.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task16.md — ScheduledActivityPause — Python — done`