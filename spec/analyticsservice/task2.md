# Task 2/2: `OrderProcessedEndpointSource`

> Rules: [`spec/rules.md`](../rules.md)

| Field | Value |
|-------|-------|
| Language | `Python` |
| Kind | `kafka-source` |
| File | `analyticsservice/src/analytics_service/internal/functions/endpoint/order_processed_endpoint_source.py` |
| Test | `analyticsservice/tests/functions/test_endpoint/order_processed_endpoint_source.py` |
| Service | `Analytics Service` |


## Behaviour

Exchange OrderProcessed events keyed by order ID.
Producers include the final status, processing time, total and confirmed item counts, and a failure reason for unsuccessful orders.
Consumers decode the event and mark its Kafka message processed only after the pipeline handles it successfully.




## Stream types
- Input: `OrderProcessed` — `model/src/model/models/order_processed.py`
- Output: `OrderProcessed` — `model/src/model/models/order_processed.py`

## Checklist

- [ ] Read [`spec/rules.md`](../rules.md), especially the `Python` section
- [ ] Open `analyticsservice/src/analytics_service/internal/functions/endpoint/order_processed_endpoint_source.py` and preserve its generated contract
- [ ] Inspect input type `OrderProcessed` in `model/src/model/models/order_processed.py`
- [ ] Inspect output type `OrderProcessed` in `model/src/model/models/order_processed.py`
- [ ] Implement every generated async method and remove `NotImplementedError`
- [ ] Run `./scripts/python/typecheck.generated.sh`
- [ ] Run `./scripts/python/test.generated.sh`
- [ ] Implement meaningful assertions in `analyticsservice/tests/functions/test_endpoint/order_processed_endpoint_source.py`
- [ ] Re-read this checklist
- [ ] Append to `spec/progress.md`: `- [x] analyticsservice/task2.md — OrderProcessedEndpointSource — Python — done`