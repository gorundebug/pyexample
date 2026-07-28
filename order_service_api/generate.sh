#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
for generator in "${ROOT}"/generate-openapi-*.sh; do
  "${generator}"
done