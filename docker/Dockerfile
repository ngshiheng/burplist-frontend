ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION}-slim AS base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.15 \
    POETRY_NO_INTERACTION=1

FROM base AS builder
ARG ENVIRONMENT
ENV ENVIRONMENT=${ENVIRONMENT}
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR app
COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN poetry install --no-root \
    $(if [ "$ENVIRONMENT" = 'production' ]; then echo '--no-dev'; fi) \
    --no-interaction --no-ansi

FROM builder AS app
COPY . /app/
CMD ["./docker/docker-entrypoint.sh"]
