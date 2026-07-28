#!/usr/bin/env bash
# Generated workspace codegen command.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"
uv run --package inventory_service_api "${ROOT}/inventory_service_api/generate.generated.sh"
uv run --package model "${ROOT}/model/generate.generated.sh"
uv run --package order_service_api "${ROOT}/order_service_api/generate.generated.sh"
