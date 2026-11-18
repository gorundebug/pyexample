# Task 9/26: `CycleAnalyticsInputSource`

> Rules: [`spec/rules.md`](../rules.md)

Paths and commands below are relative to the generated project root.

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `custom-source` |
| File | `analyticsservice/src/analytics_service/internal/functions/endpoint/cycle_analytics_input_source.py` |
| Test | `analyticsservice/tests/functions/test_endpoint/cycle_analytics_input_source.py` |
| Service | `Analytics Service` |


## Behaviour

Produce one deterministic analytics event that exercises the finite feedback cycle.




## Stream types
- Emits into graph: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`
- Receives graph result: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/endpoint/cycle_analytics_input_source.py` and preserve its generated contract
- [ ] Inspect emitted message type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Inspect graph result type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`

- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_endpoint/cycle_analytics_input_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task9.md — CycleAnalyticsInputSource — Python — done`