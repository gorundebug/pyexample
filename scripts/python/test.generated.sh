#!/usr/bin/env bash
# Generated test command.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
uv run pytest "inventoryservice/tests"
uv run pytest "orderservice/tests"
