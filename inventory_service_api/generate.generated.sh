#!/usr/bin/env bash
# Generated package codegen command.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
"${ROOT}/generate-grpc.sh"
