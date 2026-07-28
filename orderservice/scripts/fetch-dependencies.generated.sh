#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
DEPENDENCIES_DIR="${ROOT}/.servicegen/dependencies"
mkdir -p "${DEPENDENCIES_DIR}"

fetch_module() {
  local name="$1"
  local repository="$2"
  local revision="$3"
  local destination="${DEPENDENCIES_DIR}/${name}"

  if [[ -d "${destination}/.git" ]] &&
     [[ "$(git -C "${destination}" describe --tags --exact-match \
          2>/dev/null || true)" != "${revision}" ]]; then
    rm -rf "${destination}"
  fi

  if [[ ! -d "${destination}/.git" ]]; then
    rm -rf "${destination}"
    git -c advice.detachedHead=false clone --quiet --depth 1 \
      --branch "${revision}" \
      "${repository}" "${destination}"
  fi

  if [[ -x "${destination}/generate.generated.sh" ]]; then
    uv sync --quiet --project "${destination}" --extra codegen \
      --no-install-project
    PYTHON="${destination}/.venv/bin/python" \
      "${destination}/generate.generated.sh"
  fi
}

fetch_module "inventory_service_api" "https://github.com/gorundebug/pyexample-inventory-service-api.git" "v0.0.1"
fetch_module "model" "https://github.com/gorundebug/pyexample-model.git" "v0.0.1"
fetch_module "order_service_api" "https://github.com/gorundebug/pyexample-order-service-api.git" "v0.0.1"
