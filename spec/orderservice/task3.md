# Task 3/6: `ProcessOrder`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `http-source` |
| File | `orderservice/src/order_service/internal/functions/process_order.py` |
| Test | `orderservice/tests/functions/test_process_order.py` |
| Service | `Order Service` |


## Behaviour

HTTP source handler for POST /v1/processorder.
[Handler] holds timeout time.Duration read from config property 'timeout' (milliseconds, default 5000).
[HandlerState] carries a context cancel function.
[BeginRequest] attaches context timeout via WithTimeout, stores cancel in handler state.
[ConsumeMessage] decodes JSON body; validates Items non-empty and all quantities positive (write 400 and return error on failure);
generates order ID as UUID; maps each item to OrderItem (ItemId, SKU, Quantity);
reads optional CustomerId; builds Order with CreatedAt=now;
registers result callback keyed on order ID; emits Order via sc.Collect.
[Result callback] called once per result (N inventory results + possibly one TIMED_OUT);
captures in its closure: sync.Mutex mu, accumulator []OrderItemResult, responseSent bool;
locks mu on each invocation;
if responseSent return true;
if Status==TIMED_OUT compute TotalAmount as sum of item.UnitPrice*item.RequestedQty for each accumulated item, write partial response with accumulated items, call Done(), return true;
otherwise append result.ConfirmedItems to accumulator and return false if len(accumulated) < N;
when all N collected compute status (CONFIRMED if all items in accumulator have Reserved==true, else PARTIALLY_CONFIRMED),
compute TotalAmount as sum of item.UnitPrice * item.RequestedQty for each item in accumulator,
write JSON response, call Done(), return true.
[GetMessageID] returns OrderState.OrderID.
[EndRequest] cancels context.
[Private helper] converts OrderState to ProcessOrderResponse mapping all fields including optional ConfirmedItems slice.



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
- [ ] Open `orderservice/src/order_service/internal/functions/process_order.py` and preserve its generated contract
- [ ] Inspect input type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Inspect output type `OrderState` in `orderservice/src/order_service/models/order_state.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_process_order.py`
- [ ] Verify the endpoint/result lifecycle, including completion and error paths
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task3.md — ProcessOrder — Python — done`