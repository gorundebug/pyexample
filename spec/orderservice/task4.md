# Task 4/6: `ProcessOrderItem`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `grpc-sink` |
| File | `orderservice/src/order_service/internal/functions/process_order_item.py` |
| Test | `orderservice/tests/functions/test_process_order_item.py` |
| Service | `Order Service` |


## Behaviour

Outgoing unary gRPC call to the Inventory Service.
[ConsumeMessage] map OrderItem → ProcessOrderItemRequest (OrderID, ItemID, SKU, Quantity); call sender.Send(req).
[HandleResponse] map ProcessOrderItemResponse → OrderItemResult:
copy OrderID, ItemID, AvailableQty, Reserved, Status, UnitPrice from response; push downstream via sc.Collect.
[EndRequest] log the outcome.



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
- [ ] Open `orderservice/src/order_service/internal/functions/process_order_item.py` and preserve its generated contract
- [ ] Inspect input type `OrderItem` in `model/src/model/models/order_item.py`
- [ ] Inspect output type `OrderItemResult` in `model/src/model/models/order_item_result.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.sh`
- [ ] Run `./scripts/python/test.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_process_order_item.py`
- [ ] Verify the endpoint/result lifecycle, including completion and error paths
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task4.md — ProcessOrderItem — Python — done`