# Automation Service

Standalone generated Python/asyncio service.

```bash
make init            # [host] create the environment and install dependencies
make build           # [host] build the service wheel
make test            # [host] run pytest
make lint            # [host] run mypy and Ruff
make fmt             # [host] format and apply supported Ruff fixes
make docker-build    # [Docker] build the autonomous runtime image from copied sources
make docker-up       # [Docker] build and start only this service
make docker-up-dev   # [Docker] start with this directory mounted read-only
make debug DEBUG_PORT=2345 # [Docker] start debugpy using this host port
make docker-down     # [Docker] stop the standalone runtime stack
make docker-down-dev # [Docker] stop the standalone development stack
make docker-clean    # [Docker] stop the service and remove its volumes
make clean           # [host] remove Python build/cache artifacts
make help            # [host] list generated targets
```

The service defaults to pinned repository packages (`USE_LOCAL_MODULES=0`). A
generated project invokes it with `USE_LOCAL_MODULES=1`. For a separately
obtained service plus unpublished modules, place those modules next to this
directory using their generated names and select local mode explicitly:

```bash
make build USE_LOCAL_MODULES=1
make docker-build USE_LOCAL_MODULES=1
```

After publishing and pinning the packages, omit the flag or pass
`USE_LOCAL_MODULES=0`. Make never auto-detects sibling packages.
`DEPENDENCY_PROXY_DIR`, when present in the caller's environment, affects
downloads only and does not select local modules.
`debugpy` always listens on `2345` inside the container; `DEBUG_PORT` selects
the forwarded host port.

The default application listeners are HTTP `9094` and gRPC
`9204`. `AUTOMATION_SERVICE_HTTP_PORT` and
`AUTOMATION_SERVICE_GRPC_PORT` change the listener and
container-side mapping; the corresponding `_HOST_HTTP_PORT` and
`_HOST_GRPC_PORT` variables change only host forwarding.

## Generated service structure

The service coordinates named responsibility objects, not pipeline-owned registries.

- `streams_generated.py`: all streams, globally ordered construction, and deferred result/cycle binding.
- `makers_generated.py`: business and infrastructure constructors; custom makers keep their existing hooks.
- `functions_generated.py`: one instance per business function per service; ordered initializer groups run all members concurrently, across pipeline boundaries.
- `endpoints_generated.py`: independent endpoint adapters sharing those business functions.
- `clients_generated.py`, `servers_generated.py`, `connectors_generated.py`: transport construction and ownership; runtime connectors are not duplicated.
- `substreams_generated.py`: typed substream accessors and handles.
- `serde_generated.py`: generated serialization registrations.

Pipelines remain architecture metadata. Inter-pipeline links use the same stream
structure. Temporal creates a fresh set of makers, functions, streams and handles
for each workflow; it does not import the service's network bootstrap.