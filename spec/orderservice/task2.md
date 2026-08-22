# Task 2/8: `MapToOrderProcessed`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `orderservice/src/order_service/internal/functions/map_to_order_processed.py` |
| Test | `orderservice/tests/functions/test_map_to_order_processed.py` |
| Service | `Order Service` |


## Behaviour

Create an OrderProcessed event from the final order state.
Preserve the order ID, status, and processing time. Count all item results and reserved items; for unsuccessful orders use the final status as the failure reason.




## Stream types
- Input: `OrderState` — `orderservice/src/order_service/models/order_state.py`
- Output: `OrderProcessed` — `model/src/model/models/order_processed.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/map_to_order_processed.py` and preserve its generated contract
- [ ] Inspect input type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Inspect output type `OrderProcessed` in `model/src/model/models/order_processed.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_map_to_order_processed.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task2.md — MapToOrderProcessed — Python — done`