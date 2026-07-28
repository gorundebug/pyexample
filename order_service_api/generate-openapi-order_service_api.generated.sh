#!/usr/bin/env bash
# Generated OpenAPI codegen command.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
OUT="${ROOT}/src/order_service_api/generated/openapi/order_service_api"
rm -rf "${OUT}"
mkdir -p "${OUT}"
touch "${ROOT}/src/order_service_api/generated/openapi/__init__.py"
touch "${OUT}/__init__.py"

"${PYTHON:-python3}" -m datamodel_code_generator \
  --input "${ROOT}/openapi/orderserviceapi/orderserviceapi.generated.yaml" \
  --input-file-type openapi \
  --openapi-scopes paths schemas \
  --output "${OUT}/models.py" \
  --output-model-type pydantic_v2.BaseModel \
  --target-python-version 3.12 \
  --snake-case-field \
  --alias-generator to_camel \
  --use-standard-collections \
  --use-union-operator \
  --field-constraints \
  --allow-population-by-field-name \
  --disable-timestamp \
  --formatters builtin \
  --custom-file-header \
  '# Code generated from OpenAPI. DO NOT EDIT.'
