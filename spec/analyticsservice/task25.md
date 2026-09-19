# Task 25/26: `BuildSubstreamAnalyticsResult`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `analyticsservice/src/analytics_service/internal/functions/substreamanalytics/build_substream_analytics_result.py` |
| Test | `analyticsservice/tests/functions/test_substreamanalytics/build_substream_analytics_result.py` |
| Service | `Analytics Service` |


## Behaviour

Transform one callable SubStream input into its analytics result.




## Stream types
- Input: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`
- Output: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/substreamanalytics/build_substream_analytics_result.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Inspect output type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_substreamanalytics/build_substream_analytics_result.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task25.md — BuildSubstreamAnalyticsResult — Python — done`