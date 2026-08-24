# Task 1/3: `LocalJob`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `automationservice/src/automation_service/internal/functions/local_job.py` |
| Test | `automationservice/tests/functions/test_local_job.py` |
| Service | `Automation Service` |


## Behaviour

Create a job message identifying the local scheduled firing.




## Stream types
- Input: `ScheduleTrigger`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/local_job.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_local_job.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task1.md — LocalJob — Python — done`