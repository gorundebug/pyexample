# Task 26/36: `ProcessSequentialActivityB`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `automationservice/src/automation_service/internal/functions/automation/process_sequential_activity_b.py` |
| Test | `automationservice/tests/functions/test_automation/process_sequential_activity_b.py` |
| Service | `Automation Service` |


## Behaviour

Return sequential Activity B's typed result to its Temporal sink.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/automation/process_sequential_activity_b.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_automation/process_sequential_activity_b.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task26.md — ProcessSequentialActivityB — Python — done`