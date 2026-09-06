# Task 16/17: `MultiJoinAnalyticsEvents`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `multiJoin` |
| File | `analyticsservice/src/analytics_service/internal/functions/multijoinanalytics/multi_join_analytics_events.py` |
| Test | `analyticsservice/tests/functions/test_multijoinanalytics/multi_join_analytics_events.py` |
| Service | `Analytics Service` |


## Behaviour

Combine matching order, payment, and shipment analytics events.




## Stream types
- Output: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/multijoinanalytics/multi_join_analytics_events.py` and preserve its generated contract
- [ ] Inspect output type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_multijoinanalytics/multi_join_analytics_events.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task16.md — MultiJoinAnalyticsEvents — Python — done`