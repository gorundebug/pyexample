#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"

uv run ruff check --fix --force-exclude \
  --exclude generated \
  --exclude '*generated.py' \
  "analyticsservice/src" "inventory_service_api/src" "inventoryservice/src" "model/src" "order_service_api/src" "orderservice/src"
uv run ruff format --force-exclude \
  --exclude generated \
  --exclude '*generated.py' \
  "analyticsservice/src" "inventory_service_api/src" "inventoryservice/src" "model/src" "order_service_api/src" "orderservice/src"