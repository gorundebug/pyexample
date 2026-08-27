# Task 6/8: `MapToOrderState`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `orderservice/src/order_service/internal/functions/order/map_to_order_state.py` |
| Test | `orderservice/tests/functions/test_order/map_to_order_state.py` |
| Service | `Order Service` |


## Behaviour

Produce a TIMED_OUT order result that preserves the order ID and submitted total.
Do not add item results at this stage; results received before the timeout are included in the final response.




## Stream types
- Input: `Order` — `orderservice/src/order_service/models/order.py`
- Output: `OrderState` — `orderservice/src/order_service/models/order_state.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/order/map_to_order_state.py` and preserve its generated contract
- [ ] Inspect input type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Inspect output type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_order/map_to_order_state.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task6.md — MapToOrderState — Python — done`