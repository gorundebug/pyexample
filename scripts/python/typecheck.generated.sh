#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
uv run mypy --config-file mypy.ini --package "inventory_service_api" --package "model" --package "order_service_api" --package "inventory_service" --package "order_service"
uv run ruff check --force-exclude --exclude generated --exclude '*generated.py' "inventory_service_api/src" "model/src" "order_service_api/src" "inventoryservice/src" "orderservice/src"