# Task 1/2: `CountOrderProcessed`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `process` |
| File | `analyticsservice/src/analytics_service/internal/functions/analytics/count_order_processed.py` |
| Test | `analyticsservice/tests/functions/test_analytics/count_order_processed.py` |
| Service | `Analytics Service` |


## Behaviour

Count successful and unsuccessful orders independently, then return the event unchanged.




## Stream types
- Input: `OrderProcessed` — `model/src/model/models/order_processed.py`
- Output: `OrderProcessed` — `model/src/model/models/order_processed.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/analytics/count_order_processed.py` and preserve its generated contract
- [ ] Inspect input type `OrderProcessed` in `model/src/model/models/order_processed.py`
- [ ] Inspect output type `OrderProcessed` in `model/src/model/models/order_processed.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_analytics/count_order_processed.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task1.md — CountOrderProcessed — Python — done`