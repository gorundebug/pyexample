# Implementation Rules

These rules apply to every `spec/*/task*.md`. The generated graph and transport
contracts are the source of truth; business implementations and their tests are
user-owned extension points.

## Project invariants

- Project root: `example/`
- Graph: `example/graph/example.generated.yaml`
- Never edit a file whose name contains `generated`; those files are replaced
  during project merge.
- Never change generated signatures, topology wiring, IDs, config keys, or
  transport contracts in order to make an implementation easier.
- Change `.proto`/OpenAPI source and regenerate; never patch generated bindings.
- Preserve the message/stream context received from the framework.
- Do not keep mutable per-request state in function objects: function instances
  are created once and may process requests concurrently.
- Finish one task at a time and immediately copy its completion line to
  `spec/progress.md`.

## Services

| Service | Language | Directory |
|---------|----------|-----------|
| `Inventory Service` | `Python` | `inventoryservice/` |
| `Order Service` | `Python` | `orderservice/` |






## Python rules

- Business functions are user-owned classes whose async methods satisfy the
  protocols used by generated stream construction. Keep method names,
  parameter order and type annotations.
- Propagate `Stream`, `StreamContext` or `SinkStreamContext`; do not create a
  replacement context in the middle of a chain.
- Await collector/sender/result operations. Do not block the event loop with
  synchronous I/O.
- Use generated commands:
  - setup and API generation: `./scripts/python/setup.generated.sh`
  - regenerate contracts: `./scripts/python/generate.generated.sh`
  - strict mypy and Ruff: `./scripts/python/typecheck.generated.sh`
  - tests: `./scripts/python/test.generated.sh`
- Replace `NotImplementedError` only in user-owned function files and implement
  their `tests/functions/test_*.py` files.
- Do not modify `service_generated.py`, `config_generated.py`, generated
  protobuf modules, or generated OpenAPI models.
- Endpoint callbacks must complete their `ResultContext` according to the
  generated handler protocol; otherwise the originating request remains open.


## Endpoint and serialization rules

- External request/response types belong to protobuf/OpenAPI contracts.
- Internal stream types belong to the language backend's model package.
- Convert between external and internal types in endpoint handlers.
- Add serialization only where data crosses a process/storage boundary.
- For source endpoints, verify a real request and include the command in the
  task completion entry when the task asks for it.

## Priority of truth

1. Current task file.
2. Graph definition.
3. `.proto`/OpenAPI source contracts.
4. Generated type signatures.
5. servicelib runtime semantics for the selected language.
