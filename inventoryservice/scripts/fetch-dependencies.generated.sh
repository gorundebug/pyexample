#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
DEPENDENCIES_DIR="${ROOT}/.local-dependencies"
LOCAL_DEPENDENCIES_DIR="${LOCAL_DEPENDENCIES_DIR:-}"
mkdir -p "${DEPENDENCIES_DIR}"

fetch_module() {
  local name="$1"
  local repository="$2"
  local revision="$3"
  local repository_subdir="$4"
  local destination="${DEPENDENCIES_DIR}/${name}"

  if [[ -n "${LOCAL_DEPENDENCIES_DIR}" ]]; then
    local source="${LOCAL_DEPENDENCIES_DIR}/${name}"
    if [[ ! -d "${source}" ]]; then
      echo "Local dependency ${name} is missing: ${source}" >&2
      return 1
    fi
    local source_path destination_path=""
    source_path="$(cd -- "${source}" && pwd -P)"
    if [[ -d "${destination}" ]]; then
      destination_path="$(cd -- "${destination}" && pwd -P)"
    fi
    if [[ "${source_path}" != "${destination_path}" ]]; then
      rm -rf "${destination}"
      cp -R "${source_path}" "${destination}"
      rm -rf "${destination}/.git"
    fi
  else
    local repository_checkout="${DEPENDENCIES_DIR}/.repositories/${name}"
    mkdir -p "${DEPENDENCIES_DIR}/.repositories"
    if [[ -d "${repository_checkout}/.git" ]] &&
       [[ "$(git -C "${repository_checkout}" describe --tags --exact-match \
            2>/dev/null || true)" != "${revision}" ]]; then
      rm -rf "${repository_checkout}"
    fi

    if [[ ! -d "${repository_checkout}/.git" ]]; then
      git -c advice.detachedHead=false clone --quiet --depth 1 \
        --branch "${revision}" \
        "${repository}" "${repository_checkout}"
    fi
    local source="${repository_checkout}"
    if [[ -n "${repository_subdir}" ]]; then
      source="${repository_checkout}/${repository_subdir}"
    fi
    if [[ ! -d "${source}" ]]; then
      echo "Module ${name} is missing from ${repository} at ${repository_subdir}" >&2
      return 1
    fi
    rm -rf "${destination}"
    cp -R "${source}" "${destination}"
    rm -rf "${destination}/.git"
  fi

  if [[ -x "${destination}/generate.generated.sh" ]]; then
    uv sync --quiet --project "${destination}" --extra codegen \
      --no-install-project
    PYTHON="${destination}/.venv/bin/python" \
      "${destination}/generate.generated.sh"
  fi
}

fetch_module "inventory_service_api" "https://github.com/gorundebug/pyexample.git" "v0.2.77" "inventory_service_api"
fetch_module "model_python" "https://github.com/gorundebug/pyexample.git" "v0.2.77" "model_python"