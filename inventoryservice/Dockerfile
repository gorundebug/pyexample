FROM module-inventory_service_api-source AS module-inventory_service_api-source
FROM module-model-source AS module-model-source
FROM python:3.12-slim AS development

ARG DEPENDENCY_GITHUB_RAW_URL=https://github.com
ENV DEPENDENCY_GITHUB_RAW_URL=${DEPENDENCY_GITHUB_RAW_URL}
COPY dependency-download-mirrors.generated.env /etc/servicegen/dependency-download-mirrors.generated.env
COPY dependency-download-mirrors.env /etc/servicegen/dependency-download-mirrors.env
COPY dependency-download-env.generated.sh /usr/local/bin/servicegen-download-env
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
    python -m pip install --no-cache-dir uv

COPY . .
COPY --from=module-inventory_service_api-source / /local-dependencies/inventory_service_api
COPY --from=module-model-source / /local-dependencies/model

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
    uv sync --all-extras --no-cache; \
    uv pip install --python /workspace/.venv/bin/python \
      debugpy==1.8.17

FROM development AS runtime-builder

RUN uv sync --no-dev --no-editable --no-cache

FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/workspace/.venv/bin:$PATH

WORKDIR /workspace

COPY --from=runtime-builder /workspace/.venv /workspace/.venv
COPY --from=runtime-builder /workspace/config /workspace/config

CMD ["python", "-m", "inventory_service.main", \
     "--config", "/workspace/config/config.yaml", \
     "--overrides", "/workspace/config/docker_overrides.yaml"]