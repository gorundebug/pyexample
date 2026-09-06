# Task 12/17: `KeyPaymentsForJoin`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `keyBy` |
| File | `analyticsservice/src/analytics_service/internal/functions/joinanalytics/key_payments_for_join.py` |
| Test | `analyticsservice/tests/functions/test_joinanalytics/key_payments_for_join.py` |
| Service | `Analytics Service` |


## Behaviour

Key the payment analytics event by correlation key.




## Stream types
- Input: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`
- Output: `AnalyticsEvent` — `analyticsservice/src/analytics_service/models/analytics_event.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/joinanalytics/key_payments_for_join.py` and preserve its generated contract
- [ ] Inspect input type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Inspect output type `AnalyticsEvent` in `analyticsservice/src/analytics_service/models/analytics_event.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_joinanalytics/key_payments_for_join.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task12.md — KeyPaymentsForJoin — Python — done`