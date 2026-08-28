# Task 1/2: `ProcessOrderItemSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `grpc-source` |
| File | `inventoryservice/src/inventory_service/internal/functions/endpoint/process_order_item_source.py` |
| Test | `inventoryservice/tests/functions/test_endpoint/process_order_item_source.py` |
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
- Input: `OrderItem` — `model_python/src/model/models/order_item.py`
- Output: `OrderItemResult` — `model_python/src/model/models/order_item_result.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `inventoryservice/src/inventory_service/internal/functions/endpoint/process_order_item_source.py` and preserve its generated contract
- [ ] Inspect input type `OrderItem` in `model_python/src/model/models/order_item.py`
- [ ] Inspect output type `OrderItemResult` in `model_python/src/model/models/order_item_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `inventoryservice/tests/functions/test_endpoint/process_order_item_source.py`
- [ ] Verify the endpoint/result lifecycle, including completion and error paths
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] inventoryservice/task1.md — ProcessOrderItemSource — Python — done`