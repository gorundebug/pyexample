# Task 3/8: `ProcessOrderSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `http-source` |
| File | `orderservice/src/order_service/internal/functions/endpoint/process_order_source.py` |
| Test | `orderservice/tests/functions/test_endpoint/process_order_source.py` |
| Service | `Order Service` |


## Behaviour

Accept orders with at least one item and positive quantities; reject malformed or invalid requests as client errors.
Reuse X-Request-ID when supplied, otherwise generate an order ID. Preserve customer, item, price, and X-Trace data, and apply the configured timeout of five seconds by default.
Return one response per order. When all items finish, use CONFIRMED only if every item was reserved; otherwise use PARTIALLY_CONFIRMED. If the deadline wins, return TIMED_OUT with the item results received so far.
Calculate the total from processed item prices, falling back to the submitted total when no item result arrived, and include individual item failures in the response.



## External contract

| Field | Value |
|-------|-------|
| Format | `openapi` |
| Request | `object` |
| Response | `object` |


## Stream types
- Input: `Order` — `orderservice/src/order_service/models/order.py`
- Output: `OrderState` — `orderservice/src/order_service/models/order_state.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/endpoint/process_order_source.py` and preserve its generated contract
- [ ] Inspect input type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Inspect output type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_endpoint/process_order_source.py`
- [ ] Verify the endpoint/result lifecycle, including completion and error paths
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task3.md — ProcessOrderSource — Python — done`