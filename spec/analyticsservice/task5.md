# Task 5/17: `AnalyticsShipmentsSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `custom-source` |
| File | `analyticsservice/src/analytics_service/internal/functions/endpoint/analytics_shipments_source.py` |
| Test | `analyticsservice/tests/functions/test_endpoint/analytics_shipments_source.py` |
| Service | `Analytics Service` |


## Behaviour

Produce a deterministic shipment analytics event for the canonical multi-way join example.




## Stream types
- Input: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`
- Output: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/endpoint/analytics_shipments_source.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Inspect output type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_endpoint/analytics_shipments_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task5.md — AnalyticsShipmentsSource — Python — done`