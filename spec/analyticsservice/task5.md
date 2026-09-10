# Task 5/22: `ContinueCycleAnalytics`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `filter` |
| File | `analyticsservice/src/analytics_service/internal/functions/cycleanalytics/continue_cycle_analytics.py` |
| Test | `analyticsservice/tests/functions/test_cycleanalytics/continue_cycle_analytics.py` |
| Service | `Analytics Service` |


## Behaviour

Keep intermediate analytics events whose cycle counter is below three.




## Stream types
- Input: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/cycleanalytics/continue_cycle_analytics.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_cycleanalytics/continue_cycle_analytics.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task5.md — ContinueCycleAnalytics — Python — done`