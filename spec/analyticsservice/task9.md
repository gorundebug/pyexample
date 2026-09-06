# Task 9/17: `StandardAnalyticsSink`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `custom-sink` |
| File | `analyticsservice/src/analytics_service/internal/functions/endpoint/standard_analytics_sink.py` |
| Test | `analyticsservice/tests/functions/test_endpoint/standard_analytics_sink.py` |
| Service | `Analytics Service` |


## Behaviour

Validate and record analytics results routed to the standard Case branch.




## Stream types
- Input: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`
- Output: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/endpoint/standard_analytics_sink.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Inspect output type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_endpoint/standard_analytics_sink.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task9.md — StandardAnalyticsSink — Python — done`