# Task 1/6: `MapOrderItemResultToOrderState`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `orderservice/src/order_service/internal/functions/map_order_item_result_to_order_state.py` |
| Test | `orderservice/tests/functions/test_map_order_item_result_to_order_state.py` |
| Service | `Order Service` |


## Behaviour

Convert a single OrderItemResult into an OrderState.
Set OrderID from result.OrderID; set Status=CONFIRMED if result.Reserved==true, otherwise PARTIALLY_CONFIRMED.
Set ConfirmedItems to a single-element slice containing result.




## Stream types
- Input: `OrderItemResult` — `model/src/model/models/order_item_result.py`
- Output: `OrderState` — `orderservice/src/order_service/models/order_state.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/map_order_item_result_to_order_state.py` and preserve its generated contract
- [ ] Inspect input type `OrderItemResult` in `model/src/model/models/order_item_result.py`
- [ ] Inspect output type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.sh`
- [ ] Run `./scripts/python/test.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_map_order_item_result_to_order_state.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task1.md — MapOrderItemResultToOrderState — Python — done`