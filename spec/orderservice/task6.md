# Task 6/6: `SoftDeadline`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `delay` |
| File | `orderservice/src/order_service/internal/functions/soft_deadline.py` |
| Test | `orderservice/tests/functions/test_soft_deadline.py` |
| Service | `Order Service` |


## Behaviour

Cast stream.GetConfig() to *runtimecfg.DelayStreamConfig and convert cfg.Duration (int, milliseconds) to time.Duration — this is the safety margin.
If ctx has no deadline (ctx.Deadline() ok==false), return the margin directly.
Otherwise compute time.Until(deadline) minus the margin: if the result is negative return 0, otherwise return it.




## Stream types
- Input: `Order` — `orderservice/src/order_service/models/order.py`
- Output: `Order` — `orderservice/src/order_service/models/order.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `orderservice/src/order_service/internal/functions/soft_deadline.py` and preserve its generated contract
- [ ] Inspect input type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Inspect output type `Order` in `orderservice/src/order_service/models/order.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `orderservice/tests/functions/test_soft_deadline.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task6.md — SoftDeadline — Python — done`