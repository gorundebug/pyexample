# Task 12/20: `ProcessScheduledWorkflow`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `automationservice/src/automation_service/internal/functions/process_scheduled_workflow.py` |
| Test | `automationservice/tests/functions/test_process_scheduled_workflow.py` |
| Service | `Automation Service` |


## Behaviour

Return the visible result of one scheduled Workflow execution.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/process_scheduled_workflow.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_process_scheduled_workflow.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task12.md — ProcessScheduledWorkflow — Python — done`