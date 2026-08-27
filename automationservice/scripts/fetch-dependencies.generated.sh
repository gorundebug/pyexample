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
  fi

  if [[ -x "${destination}/generate.generated.sh" ]]; then
    uv sync --quiet --project "${destination}" --extra codegen \
      --no-install-project
    PYTHON="${destination}/.venv/bin/python" \
      "${destination}/generate.generated.sh"
  fi
}