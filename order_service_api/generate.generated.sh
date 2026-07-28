#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
for generator in "${ROOT}"/generate-openapi-*.generated.sh; do
  "${generator}"
done