# Task 12/13: `TemporalWorkflowSchedule`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `schedule-source` |
| File | `automationservice/src/automation_service/internal/functions/temporal_workflow_schedule.py` |
| Test | `automationservice/tests/functions/test_temporal_workflow_schedule.py` |
| Service | `Automation Service` |


## Behaviour

Create a Workflow job message identifying the durable scheduled firing.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/temporal_workflow_schedule.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_temporal_workflow_schedule.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task12.md — TemporalWorkflowSchedule — Python — done`