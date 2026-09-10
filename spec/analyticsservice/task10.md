# Task 10/22: `CycleAnalyticsResultSink`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `custom-sink` |
| File | `analyticsservice/src/analytics_service/internal/functions/endpoint/cycle_analytics_result_sink.py` |
| Test | `analyticsservice/tests/functions/test_endpoint/cycle_analytics_result_sink.py` |
| Service | `Analytics Service` |


## Behaviour

Validate the terminal event emitted after three passes through the feedback cycle.




## Stream types
- Input: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`
- Output: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/endpoint/cycle_analytics_result_sink.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Inspect output type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_endpoint/cycle_analytics_result_sink.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task10.md — CycleAnalyticsResultSink — Python — done`