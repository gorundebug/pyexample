#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
uv run pytest "analyticsservice/tests"
uv run pytest "inventoryservice/tests"
uv run pytest "orderservice/tests"