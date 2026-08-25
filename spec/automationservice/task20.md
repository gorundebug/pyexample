# Task 20/20: `WorkflowPause`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `delay` |
| File | `automationservice/src/automation_service/internal/functions/workflow_pause.py` |
| Test | `automationservice/tests/functions/test_workflow_pause.py` |
| Service | `Automation Service` |


## Behaviour

Use the same Delay contract backed by the Temporal Workflow timer.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/workflow_pause.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_workflow_pause.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task20.md — WorkflowPause — Python — done`