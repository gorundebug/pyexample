# Task 4/8: `MapOrderItemResultToOrderState`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `orderservice/src/order_service/internal/functions/order/map_order_item_result_to_order_state.py` |
| Test | `orderservice/tests/functions/test_order/map_order_item_result_to_order_state.py` |
| Service | `Order Service` |


## Behaviour

Produce an order result containing one inventory result and preserving its order ID.
Mark it CONFIRMED when the item was reserved; otherwise mark it PARTIALLY_CONFIRMED.
Record the time when this result is produced.




## Stream types
- Input: `OrderItemResult` — `model_python/src/model/models/order_item_result.py`
- Output: `OrderState` — `orderservice/src/order_service/models/order_state.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/order/map_order_item_result_to_order_state.py` and preserve its generated contract
- [ ] Inspect input type `OrderItemResult` in `model_python/src/model/models/order_item_result.py`
- [ ] Inspect output type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_order/map_order_item_result_to_order_state.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task4.md — MapOrderItemResultToOrderState — Python — done`