# Task 2/6: `MapToOrderState`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `orderservice/src/order_service/internal/functions/map_to_order_state.py` |
| Test | `orderservice/tests/functions/test_map_to_order_state.py` |
| Service | `Order Service` |


## Behaviour

Convert an Order that reached the soft deadline into an OrderState.
Set OrderID from Order.ID; set Status to TIMED_OUT; leave ConfirmedItems nil.




## Stream types
- Input: `Order` — `orderservice/src/order_service/models/order.py`
- Output: `OrderState` — `orderservice/src/order_service/models/order_state.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/map_to_order_state.py` and preserve its generated contract
- [ ] Inspect input type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Inspect output type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_map_to_order_state.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task2.md — MapToOrderState — Python — done`