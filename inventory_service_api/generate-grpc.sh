#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
OUT="${ROOT}/src/inventory_service_api/generated"
rm -rf "${OUT}"
mkdir -p "${OUT}"

PROTO_FILES=()
while IFS= read -r file; do
  PROTO_FILES+=("${file}")
done < <(find "${ROOT}/proto" -type f -name '*.proto' | sort)

"${PYTHON:-python3}" -m grpc_tools.protoc \
  -I "${ROOT}" \
  --python_out="${OUT}" \
  --pyi_out="${OUT}" \
  --grpc_python_out="${OUT}" \
  "${PROTO_FILES[@]}"

find "${OUT}" -type d -exec touch '{}/__init__.py' \;

# protoc emits imports rooted at the proto tree. Qualify them with this
# installable package so generated modules also work outside the source tree.
find "${OUT}" -type f \( -name '*_pb2*.py' -o -name '*_pb2*.pyi' \) -exec \
  sed -i.bak -E \
  's/^from (proto(\.[A-Za-z0-9_]+)*) import /from inventory_service_api.generated.\1 import /' \
  '{}' \;
find "${OUT}" -name '*.bak' -delete