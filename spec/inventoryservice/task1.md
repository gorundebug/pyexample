# Task 1/2: `GetInventoryItemData`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `process` |
| File | `inventoryservice/src/inventory_service/internal/functions/get_inventory_item_data.py` |
| Test | `inventoryservice/tests/functions/test_get_inventory_item_data.py` |
| Service | `Inventory Service` |


## Behaviour

Look up the inventory record by OrderItem.SKU; retrieve current stock and UnitPrice from the record.
Always copy OrderID, ItemID, SKU, RequestedQty (=OrderItem.Quantity), UnitPrice into the result.
If stock >= OrderItem.Quantity: reserve the stock atomically and emit
OrderItemResult{OrderID, ItemID, SKU, RequestedQty, UnitPrice, Reserved: true, Status: CONFIRMED, AvailableQty: OrderItem.Quantity} via out.
If stock is insufficient: emit
OrderItemResult{OrderID, ItemID, SKU, RequestedQty, UnitPrice, Reserved: false, Status: OUT_OF_STOCK, AvailableQty: actual available} via rout.




## Stream types
- Input: `OrderItem` — `model/src/model/models/order_item.py`
- Output: `OrderItemResult` — `model/src/model/models/order_item_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `inventoryservice/src/inventory_service/internal/functions/get_inventory_item_data.py` and preserve its generated contract
- [ ] Inspect input type `OrderItem` in `model/src/model/models/order_item.py`
- [ ] Inspect output type `OrderItemResult` in `model/src/model/models/order_item_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.sh`
- [ ] Run `./scripts/python/test.sh`
- [ ] Implement meaningful assertions in `inventoryservice/tests/functions/test_get_inventory_item_data.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] inventoryservice/task1.md — GetInventoryItemData — Python — done`