# Analytics Service

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

The default application listeners are HTTP `9093` and gRPC
`9203`. `ANALYTICS_SERVICE_HTTP_PORT` and
`ANALYTICS_SERVICE_GRPC_PORT` change the listener and
container-side mapping; the corresponding `_HOST_HTTP_PORT` and
`_HOST_GRPC_PORT` variables change only host forwarding.
