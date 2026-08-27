# Task 21/36: `ProcessFanoutActivityB`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `automationservice/src/automation_service/internal/functions/automation/process_fanout_activity_b.py` |
| Test | `automationservice/tests/functions/test_automation/process_fanout_activity_b.py` |
| Service | `Automation Service` |


## Behaviour

Return Activity B's typed fan-out result.




## Stream types

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `automationservice/src/automation_service/internal/functions/automation/process_fanout_activity_b.py` and preserve its generated contract
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `automationservice/tests/functions/test_automation/process_fanout_activity_b.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] automationservice/task21.md — ProcessFanoutActivityB — Python — done`