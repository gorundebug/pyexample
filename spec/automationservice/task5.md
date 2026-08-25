# Task 5/20: `ObserveFanoutActivityC`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `automationservice/src/automation_service/internal/functions/observe_fanout_activity_c.py` |
| Test | `automationservice/tests/functions/test_observe_fanout_activity_c.py` |
| Service | `Automation Service` |


## Behaviour

Observe the typed result returned by the Activity C fan-out branch.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/observe_fanout_activity_c.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_observe_fanout_activity_c.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task5.md — ObserveFanoutActivityC — Python — done`