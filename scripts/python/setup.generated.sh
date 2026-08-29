#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "${ROOT}"

for service in analyticsservice automationservice inventoryservice orderservice ; do
  LOCAL_DEPENDENCIES_DIR="${ROOT}" \
    "${ROOT}/${service}/scripts/fetch-dependencies.generated.sh"
done

if [[ ! -d .pyservicelib/.git ]]; then
  if [[ -e .pyservicelib ]]; then
    echo ".pyservicelib exists but is not a Git checkout" >&2
    exit 1
  fi
  git clone --branch "v0.2.30" \
    --depth 1 \
    "https://github.com/gorundebug/pyservicelib.git" \
    .pyservicelib
fi

uv sync --all-packages --all-extras
"${ROOT}/scripts/python/generate.generated.sh"