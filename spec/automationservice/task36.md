# Task 36/36: `WorkflowJobEndpointSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `temporal-source` |
| File | `automationservice/src/automation_service/internal/functions/workflow/workflow_job_endpoint_source.py` |
| Test | `automationservice/tests/functions/test_workflow/workflow_job_endpoint_source.py` |
| Service | `Automation Service` |





## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/workflow/workflow_job_endpoint_source.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_workflow/workflow_job_endpoint_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task36.md — WorkflowJobEndpointSource — Python — done`