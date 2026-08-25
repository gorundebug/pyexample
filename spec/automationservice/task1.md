# Task 1/4: `DurablePause`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `delay` |
| File | `automationservice/src/automation_service/internal/functions/durable_pause.py` |
| Test | `automationservice/tests/functions/test_durable_pause.py` |
| Service | `Automation Service` |


## Behaviour

Suspend a DurableCall through a Temporal timer, then resume the pipeline without occupying an Activity slot.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/durable_pause.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_durable_pause.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task1.md — DurablePause — Python — done`