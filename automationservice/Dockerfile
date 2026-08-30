ARG DEPENDENCY_DOCKER_REGISTRY=docker.io
FROM pyservicelib-source AS pyservicelib-source
FROM module-model_python-source AS module-model_python-source
FROM ${DEPENDENCY_DOCKER_REGISTRY}/library/python:3.12-slim-bookworm AS development

ARG DEPENDENCY_GITHUB_RAW_URL=https://github.com
ENV DEPENDENCY_GITHUB_RAW_URL=${DEPENDENCY_GITHUB_RAW_URL}
COPY dependency-download-mirrors.generated.env /etc/servicegen/dependency-download-mirrors.generated.env
COPY dependency-download-mirrors.env /etc/servicegen/dependency-download-mirrors.env
COPY dependency-download-env.generated.sh /usr/local/bin/servicegen-download-env
COPY prepare-local-build.generated.sh /usr/local/bin/prepare-local-build
SHELL ["/usr/local/bin/servicegen-download-env", "/bin/sh", "-c"]

ARG PIP_INDEX_URL=https://pypi.org/simple
ARG PIP_TRUSTED_HOST=
ARG UV_INDEX_URL=https://pypi.org/simple
ARG GIT_CONFIG_COUNT=0
ARG GIT_CONFIG_KEY_0=
ARG GIT_CONFIG_VALUE_0=
ARG GIT_CONFIG_KEY_1=
ARG GIT_CONFIG_VALUE_1=
ARG DEPENDENCY_APT_DEBIAN_URL=
ARG DEPENDENCY_APT_DEBIAN_SECURITY_URL=
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PATH=/workspace/.venv/bin:$PATH \
    PIP_INDEX_URL=${PIP_INDEX_URL} \
    PIP_TRUSTED_HOST=${PIP_TRUSTED_HOST} \
    UV_INDEX_URL=${UV_INDEX_URL}
ENV GIT_CONFIG_COUNT=${GIT_CONFIG_COUNT} \
    GIT_CONFIG_KEY_0=${GIT_CONFIG_KEY_0} \
    GIT_CONFIG_VALUE_0=${GIT_CONFIG_VALUE_0} \
    GIT_CONFIG_KEY_1=${GIT_CONFIG_KEY_1} \
    GIT_CONFIG_VALUE_1=${GIT_CONFIG_VALUE_1}

WORKDIR /workspace

RUN if [ -n "$DEPENDENCY_APT_DEBIAN_URL$DEPENDENCY_APT_DEBIAN_SECURITY_URL" ]; then \
      find /etc/apt -type f \( -name '*.list' -o -name '*.sources' \) -exec sed -i \
        -e "s|http://deb.debian.org/debian-security|$DEPENDENCY_APT_DEBIAN_SECURITY_URL|g" \
        -e "s|http://deb.debian.org/debian|$DEPENDENCY_APT_DEBIAN_URL|g" {} +; \
    fi
RUN apt-get update && \
    apt-get install --yes --no-install-recommends git ca-certificates && \
    rm -rf /var/lib/apt/lists/* && \
    python -m pip install --no-cache-dir uv==0.12.7

COPY . .
COPY --from=pyservicelib-source / /tmp/pyservicelib-source
RUN set -eu; \
    source_dir=/tmp/pyservicelib-source; \
    archive=$(find "$source_dir" -mindepth 1 -maxdepth 1 -type f \( -name context -o -name '*.tar' -o -name '*.tar.gz' -o -name '*.tgz' -o -name '*.tar.xz' \) -print -quit); \
    if [ -n "$archive" ]; then \
      mkdir -p /tmp/pyservicelib-archive; \
      tar -xf "$archive" -C /tmp/pyservicelib-archive; \
      source_dir=/tmp/pyservicelib-archive; \
    fi; \
    manifest="$source_dir/pyproject.toml"; \
    if [ ! -f "$manifest" ]; then manifest=$(find "$source_dir" -mindepth 2 -maxdepth 2 -type f -name pyproject.toml -print -quit); fi; \
    if [ -z "$manifest" ] || [ ! -f "$manifest" ]; then echo "pyservicelib source context has no pyproject.toml" >&2; exit 1; fi; \
    source_dir=${manifest%/pyproject.toml}; \
    mkdir -p /local-dependencies/pyservicelib; \
    cp -a "$source_dir/." /local-dependencies/pyservicelib/; \
    rm -rf /tmp/pyservicelib-source /tmp/pyservicelib-archive
COPY --from=module-model_python-source / /tmp/module-model_python-source
RUN set -eu; \
    source_dir=/tmp/module-model_python-source; \
    archive=$(find "$source_dir" -mindepth 1 -maxdepth 1 -type f \( -name context -o -name '*.tar' -o -name '*.tar.gz' -o -name '*.tgz' -o -name '*.tar.xz' \) -print -quit); \
    if [ -n "$archive" ]; then \
      mkdir -p /tmp/module-model_python-archive; \
      tar -xf "$archive" -C /tmp/module-model_python-archive; \
      source_dir=/tmp/module-model_python-archive; \
    fi; \
    manifest=$(find "$source_dir" -type f -path '*/model_python/pyproject.toml' -print -quit); \
    if [ -z "$manifest" ]; then manifest="$source_dir/pyproject.toml"; fi; \
    if [ ! -f "$manifest" ]; then manifest=$(find "$source_dir" -mindepth 2 -maxdepth 2 -type f -name pyproject.toml -print -quit); fi; \
    if [ -z "$manifest" ] || [ ! -f "$manifest" ]; then echo "module model_python source context has no pyproject.toml" >&2; exit 1; fi; \
    source_dir=${manifest%/pyproject.toml}; \
    mkdir -p /local-dependencies/model_python; \
    cp -a "$source_dir/." /local-dependencies/model_python/; \
    rm -rf /tmp/module-model_python-source /tmp/module-model_python-archive

RUN --mount=type=secret,id=github_token,required=false \
    --mount=type=secret,id=gitlab_token,required=false \
    set -eu; \
    trap 'rm -f /root/.gitconfig' EXIT; \
    if [ -s /run/secrets/github_token ]; then \
      token="$(cat /run/secrets/github_token)"; \
      git config --global \
        url."https://x-access-token:${token}@github.com/".insteadOf \
        "https://github.com/"; \
    fi; \
    if [ -s /run/secrets/gitlab_token ]; then \
      token="$(cat /run/secrets/gitlab_token)"; \
      git config --global \
        url."https://oauth2:${token}@gitlab.com/".insteadOf \
        "https://gitlab.com/"; \
    fi; \
    LOCAL_DEPENDENCIES_DIR=/local-dependencies ./scripts/fetch-dependencies.generated.sh; \
    sed -i \
      's|^pyservicelib-gorundebug = { git = .* }$|pyservicelib-gorundebug = { path = "/local-dependencies/pyservicelib" }|' \
      pyproject.toml; \
    sed -i \
      's|^model = { workspace = true }$|model = { path = ".local-dependencies/model_python" }|' \
      pyproject.toml; \
    uv sync --all-extras --no-cache; \
    uv pip install --python /workspace/.venv/bin/python \
      debugpy==1.8.17

FROM development AS runtime-builder

RUN uv sync --no-dev --no-editable --no-cache

FROM ${DEPENDENCY_DOCKER_REGISTRY}/library/python:3.12-slim-bookworm AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/workspace/.venv/bin:$PATH

WORKDIR /workspace

COPY --from=runtime-builder /workspace/.venv /workspace/.venv
COPY --from=runtime-builder /workspace/config /workspace/config

ENTRYPOINT ["python", "-m", "automation_service.main"]
CMD ["--config", "/workspace/config/config.yaml", \
     "--values", "/workspace/config/overrides.yaml", \
     "--overrides", "/workspace/config/docker_overrides.yaml"]