# Task 8/8: `SoftDeadline`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `delay` |
| File | `orderservice/src/order_service/internal/functions/soft_deadline.py` |
| Test | `orderservice/tests/functions/test_soft_deadline.py` |
| Service | `Order Service` |


## Behaviour

Trigger the timeout branch shortly before the request deadline, leaving the configured duration to assemble a response.
When no request deadline exists, use the configured duration itself. Never wait past an existing deadline.




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
- [ ] Append to `spec/progress.md`: `- [x] orderservice/task8.md — SoftDeadline — Python — done`