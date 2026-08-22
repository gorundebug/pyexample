# Task 2/2: `ProcessOrderItem`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `grpc-source` |
| File | `inventoryservice/src/inventory_service/internal/functions/process_order_item.py` |
| Test | `inventoryservice/tests/functions/test_process_order_item.py` |
| Service | `Inventory Service` |


## Behaviour

Reserve inventory for one order item using its order ID, item ID, SKU, and quantity.
Return the available quantity, reservation outcome, and status. The caller combines this response with the original identity, requested quantity, and unit price.
If the inventory call fails, the caller returns a non-reserved PROCESSING_ERROR result with the failure message.



## External contract

| Field | Value |
|-------|-------|
| Format | `proto` |
| Request | `ProcessOrderItemRequest` |
| Response | `ProcessOrderItemResponse` |


## Stream types
- Input: `OrderItem` — `model/src/model/models/order_item.py`
- Output: `OrderItemResult` — `model/src/model/models/order_item_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `inventoryservice/src/inventory_service/internal/functions/process_order_item.py` and preserve its generated contract
- [ ] Inspect input type `OrderItem` in `model/src/model/models/order_item.py`
- [ ] Inspect output type `OrderItemResult` in `model/src/model/models/order_item_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `inventoryservice/tests/functions/test_process_order_item.py`
- [ ] Verify the endpoint/result lifecycle, including completion and error paths
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] inventoryservice/task2.md — ProcessOrderItem — Python — done`
