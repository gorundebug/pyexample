# Task 1/36: `ActivityJobEndpointSink`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `temporal-sink` |
| File | `automationservice/src/automation_service/internal/functions/activity/activity_job_endpoint_sink.py` |
| Test | `automationservice/tests/functions/test_activity/activity_job_endpoint_sink.py` |
| Service | `Automation Service` |





## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/activity/activity_job_endpoint_sink.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_activity/activity_job_endpoint_sink.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task1.md — ActivityJobEndpointSink — Python — done`