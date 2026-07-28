#!/usr/bin/env bash
set -euo pipefail

if (($# != 2)); then
  echo "usage: $0 <service-directory> <output-directory>" >&2
  exit 2
fi

service_dir="${1%/}"
output_dir="${2%/}"
service_name="$(basename "${service_dir}")"
overlay_dir=".servicegen/python-services/${service_name}"

if [[ ! -f "${service_dir}/pyproject.toml" ]]; then
  echo "Python service directory does not contain pyproject.toml: ${service_dir}" >&2
  exit 1
fi
if [[ ! -d "${overlay_dir}" ]]; then
  echo "Python service publishing overlay is missing: ${overlay_dir}" >&2
  exit 1
fi
if [[ -e "${output_dir}" &&
      -n "$(find "${output_dir}" -mindepth 1 -maxdepth 1 -print -quit)" ]]; then
  echo "output directory must be empty: ${output_dir}" >&2
  exit 1
fi

mkdir -p "${output_dir}"
cp -R "${service_dir}/." "${output_dir}/"

for file in .dockerignore; do
  if [[ -f "${file}" ]]; then
    cp "${file}" "${output_dir}/${file}"
  fi
done

# Apply service-specific entrypoints last. Overlay filenames make generated
# ownership explicit; published repositories receive conventional names.
cp "${overlay_dir}/pyproject.generated.toml" \
  "${output_dir}/pyproject.toml"
cp "${overlay_dir}/Makefile" "${output_dir}/Makefile"
cp "${overlay_dir}/make.generated.mk" "${output_dir}/make.generated.mk"
cp "${overlay_dir}/Dockerfile.generated" "${output_dir}/Dockerfile"
cp "${overlay_dir}/docker-compose.generated.yml" \
  "${output_dir}/docker-compose.yml"
cp "${overlay_dir}/gitignore.generated" "${output_dir}/.gitignore"
mkdir -p "${output_dir}/scripts"
cp "${overlay_dir}/fetch-dependencies.generated.sh" \
  "${output_dir}/scripts/fetch-dependencies.generated.sh"

echo "Packaged standalone Python service ${service_name} in ${output_dir}"