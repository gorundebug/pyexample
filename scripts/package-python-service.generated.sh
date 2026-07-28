#!/usr/bin/env bash
set -euo pipefail

if (($# != 2)); then
  echo "usage: $0 <service-directory> <output-directory>" >&2
  exit 2
fi

service_dir="${1%/}"
output_dir="${2%/}"
service_name="$(basename "${service_dir}")"

if [[ ! -f "${service_dir}/pyproject.toml" ]]; then
  echo "Python service directory does not contain pyproject.toml: ${service_dir}" >&2
  exit 1
fi
for file in pyproject.standalone.generated.toml Makefile \
  make.generated.mk Dockerfile.generated docker-compose.generated.yml \
  gitignore.generated scripts/fetch-dependencies.generated.sh; do
  if [[ ! -f "${service_dir}/${file}" ]]; then
    echo "Python service publishing file is missing: ${service_dir}/${file}" >&2
    exit 1
  fi
done
if [[ -e "${output_dir}" &&
      -n "$(find "${output_dir}" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "output directory must be empty: ${output_dir}" >&2
  exit 1
fi

mkdir -p "${output_dir}"
cp -R "${service_dir}/." "${output_dir}/"
find "${output_dir}" -type d \( \
  -name .mypy_cache -o \
  -name .pytest_cache -o \
  -name .ruff_cache -o \
  -name __pycache__ \
\) -prune -exec rm -rf {} +
find "${output_dir}" -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete

for file in .dockerignore; do
  if [[ -f "${file}" ]]; then
    cp "${file}" "${output_dir}/${file}"
  fi
done

# Alternative standalone inputs live next to the service they describe.
# Published repositories receive conventional root filenames.
cp "${service_dir}/pyproject.standalone.generated.toml" \
  "${output_dir}/pyproject.toml"
cp "${service_dir}/Dockerfile.generated" "${output_dir}/Dockerfile"
cp "${service_dir}/docker-compose.generated.yml" \
  "${output_dir}/docker-compose.yml"
cp "${service_dir}/gitignore.generated" "${output_dir}/.gitignore"
rm -f "${output_dir}/pyproject.standalone.generated.toml" \
  "${output_dir}/Dockerfile.generated" \
  "${output_dir}/docker-compose.generated.yml" \
  "${output_dir}/gitignore.generated"

echo "Packaged standalone Python service ${service_name} in ${output_dir}"