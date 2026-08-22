# Python Servicegen Example

Self-contained Python/asyncio implementation of the generated order-processing
example. The repository contains three independent services and their model,
OpenAPI, and protobuf contract packages.

## Services

- `inventoryservice` — gRPC inventory reservation service.
- `orderservice` — HTTP order-processing service.
- `analyticsservice` — Kafka consumer that counts successful and unsuccessful orders.

## Contract packages

- `inventory_service_api`
- `order_service_api`
- `model`

## Run with Docker

```bash
make docker-up
```

For minimal images without source mounts, editable packages, test dependencies,
or the `uv` build tool, run `make docker-up RUNTIME_IMAGE=1`. Benchmark and
profiling tools select this mode automatically. Plain `make docker-up` keeps the
development layout.

## Optional order analytics through Kafka

The shared `orderProcessed` Kafka endpoint is disabled in Order Service by
default and creates no producer while disabled. Enable it in
`orderservice/config/overrides.yaml`:

```yaml
endpoints:
  orderProcessed:
    enabled: true
```

The Analytics Service then consumes `order-processed` from the included
Redpanda broker.

Submit an order that can be reserved from the initial inventory:

```bash
curl --fail-with-body \
  -X POST http://localhost:9091/v1/processorder \
  -H 'Content-Type: application/json' \
  -d '{
    "customer_id": "customer-1",
    "items": [
      {
        "item_id": "item-1",
        "sku": "SKU-001",
        "quantity": 2,
        "unit_price": 799.0
      }
    ]
  }'
```

The response has order status `CONFIRMED`; its item has `reserved: true` and
status `CONFIRMED`. Initial inventory is `SKU-001: 100`, `SKU-002: 50`, and
`SKU-003: 25`. Successful requests reduce that inventory until the Inventory
Service is restarted.

Run the integration scenario:

```bash
make integration-test
```

Stop the services:

```bash
make docker-down
```

Use `make help` to see all generated build, test, type-checking, formatting,
and observability commands.

The source architecture used to generate the project is available in
`graph/example.generated.yaml`.
