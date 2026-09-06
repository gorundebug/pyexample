# Task 10/17: `JoinOrderPaymentAnalytics`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `join` |
| File | `analyticsservice/src/analytics_service/internal/functions/joinanalytics/join_order_payment_analytics.py` |
| Test | `analyticsservice/tests/functions/test_joinanalytics/join_order_payment_analytics.py` |
| Service | `Analytics Service` |


## Behaviour

Join matching order and payment analytics events and emit their combined total.




## Stream types
- Output: `AnalyticsResult` — `analyticsservice/src/analytics_service/models/analytics_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/joinanalytics/join_order_payment_analytics.py` and preserve its generated contract
- [ ] Inspect output type `AnalyticsResult` in `analyticsservice/src/analytics_service/models/analytics_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_joinanalytics/join_order_payment_analytics.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task10.md — JoinOrderPaymentAnalytics — Python — done`