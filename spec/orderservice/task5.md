# Task 5/6: `ProcessOrderItems`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `flatMap` |
| File | `orderservice/src/order_service/internal/functions/process_order_items.py` |
| Test | `orderservice/tests/functions/test_process_order_items.py` |
| Service | `Order Service` |


## Behaviour

Expand an Order into individual OrderItem messages — one sc.Collect call per element of Order.Items.
Copy Order.ID into each emitted OrderItem.OrderID.




## Stream types
- Input: `Order` — `orderservice/src/order_service/models/order.py`
- Output: `OrderItem` — `model/src/model/models/order_item.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/process_order_items.py` and preserve its generated contract
- [ ] Inspect input type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Inspect output type `OrderItem` in `model/src/model/models/order_item.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_process_order_items.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task5.md — ProcessOrderItems — Python — done`