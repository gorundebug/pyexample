# Analytics Service

Standalone generated Python/asyncio service.

```bash
make init            # create the environment and install dependencies
make build           # build the service wheel
make test            # run pytest
make lint            # run mypy and Ruff
make fmt             # format and apply supported Ruff fixes
make docker-build    # build the autonomous runtime image from copied sources
make docker-up       # build and start only this service
make docker-up-dev   # start with this directory mounted read-only
make debug DEBUG_PORT=2345 # start debugpy using this host port
make docker-down
make docker-down-dev
make docker-clean    # stop the service and remove its volumes
make clean           # remove Python build/cache artifacts
make help
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