# Task 26/26: `InvokeAnalyticsSubstream`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `analyticsservice/src/analytics_service/internal/functions/substreamanalytics/invoke_analytics_substream.py` |
| Test | `analyticsservice/tests/functions/test_substreamanalytics/invoke_analytics_substream.py` |
| Service | `Analytics Service` |


## Behaviour

Invoke the service-local analytics SubStream and emit its returned result.




## Stream types
- Input: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`
- Output: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/substreamanalytics/invoke_analytics_substream.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Inspect output type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_substreamanalytics/invoke_analytics_substream.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task26.md — InvokeAnalyticsSubstream — Python — done`