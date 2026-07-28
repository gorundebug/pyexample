#!/usr/bin/env bash
# Generated integration test command.
set -euo pipefail

ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
COMPOSE_FILE="${ROOT}/docker-compose.yml"

cleanup() {
  docker compose -f "${COMPOSE_FILE}" down --remove-orphans
}
trap cleanup EXIT

docker compose -f "${COMPOSE_FILE}" up -d --build inventoryservice orderservice

python3 - <<'PY'
import time
import urllib.request

targets = [
    "http://127.0.0.1:9092/status",
    "http://127.0.0.1:9091/status",
]
for target in targets:
    for attempt in range(120):
        try:
            with urllib.request.urlopen(target, timeout=2) as response:
                if response.status < 500:
                    break
        except OSError:
            if attempt == 119:
                raise
            time.sleep(0.25)
PY

if [[ -n "${SERVICEGEN_INTEGRATION_COMMAND:-}" ]]; then
  /bin/bash -lc "${SERVICEGEN_INTEGRATION_COMMAND}"
fi

# SIGTERM exercises generated stop_service() and its bounded named shutdown.
docker compose -f "${COMPOSE_FILE}" stop --timeout 35 inventoryservice orderservice
