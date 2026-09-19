# Task 3/3: `GetInventoryItemError`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `map` |
| File | `inventoryservice/src/inventory_service/internal/functions/inventory_item/get_inventory_item_error.py` |
| Test | `inventoryservice/tests/functions/test_inventory_item/get_inventory_item_error.py` |
| Service | `Inventory Service` |


## Behaviour

When inventory processing fails, return an OUT_OF_STOCK result with no available quantity.
Preserve the order and item identity and requested quantity, and record the failure.




## Stream types
- Output: `OrderItemResult` — `model_python/src/model/models/order_item_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `inventoryservice/src/inventory_service/internal/functions/inventory_item/get_inventory_item_error.py` and preserve its generated contract
- [ ] Inspect output type `OrderItemResult` in `model_python/src/model/models/order_item_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `inventoryservice/tests/functions/test_inventory_item/get_inventory_item_error.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] inventoryservice/task3.md — GetInventoryItemError — Python — done`