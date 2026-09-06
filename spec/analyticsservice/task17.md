# Task 17/17: `RouteAnalyticsResult`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `case` |
| File | `analyticsservice/src/analytics_service/internal/functions/multijoinanalytics/route_analytics_result.py` |
| Test | `analyticsservice/tests/functions/test_multijoinanalytics/route_analytics_result.py` |
| Service | `Analytics Service` |


## Behaviour

Route high-value analytics results to the first branch and all others to the second branch.




## Stream types
- Input: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/multijoinanalytics/route_analytics_result.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_multijoinanalytics/route_analytics_result.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task17.md — RouteAnalyticsResult — Python — done`