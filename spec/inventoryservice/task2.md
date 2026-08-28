# Task 2/2: `GetInventoryItemData`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `process` |
| File | `inventoryservice/src/inventory_service/internal/functions/inventory_item/get_inventory_item_data.py` |
| Test | `inventoryservice/tests/functions/test_inventory_item/get_inventory_item_data.py` |
| Service | `Inventory Service` |


## Behaviour

Reserve the requested quantity without allowing concurrent orders to overdraw stock.
On success, return CONFIRMED with the requested quantity available. Otherwise return OUT_OF_STOCK with the current available quantity.
Preserve the order and item identity, requested quantity, and unit price.
The example starts with SKU-001: 100, SKU-002: 50, and SKU-003: 25.




## Stream types
- Input: `OrderItem` — `model_python/src/model/models/order_item.py`
- Output: `OrderItemResult` — `model_python/src/model/models/order_item_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `inventoryservice/src/inventory_service/internal/functions/inventory_item/get_inventory_item_data.py` and preserve its generated contract
- [ ] Inspect input type `OrderItem` in `model_python/src/model/models/order_item.py`
- [ ] Inspect output type `OrderItemResult` in `model_python/src/model/models/order_item_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `inventoryservice/tests/functions/test_inventory_item/get_inventory_item_data.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] inventoryservice/task2.md — GetInventoryItemData — Python — done`