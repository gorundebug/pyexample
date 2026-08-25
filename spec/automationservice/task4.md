# Task 4/13: `ObserveWorkflowResult`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `automationservice/src/automation_service/internal/functions/observe_workflow_result.py` |
| Test | `automationservice/tests/functions/test_observe_workflow_result.py` |
| Service | `Automation Service` |


## Behaviour

Preserve the result returned through the on-demand Workflow endpoint.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/observe_workflow_result.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_observe_workflow_result.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task4.md — ObserveWorkflowResult — Python — done`