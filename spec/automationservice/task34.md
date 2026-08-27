# Task 34/36: `TemporalWorkflowScheduleSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `schedule-source` |
| File | `automationservice/src/automation_service/internal/functions/workflow/temporal_workflow_schedule_source.py` |
| Test | `automationservice/tests/functions/test_workflow/temporal_workflow_schedule_source.py` |
| Service | `Automation Service` |


## Behaviour

Create a Workflow job message identifying the durable scheduled firing.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/workflow/temporal_workflow_schedule_source.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_workflow/temporal_workflow_schedule_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task34.md — TemporalWorkflowScheduleSource — Python — done`