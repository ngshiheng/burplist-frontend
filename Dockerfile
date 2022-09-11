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
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR app
COPY pyproject.toml /app/
COPY poetry.lock /app/
RUN poetry install --no-root --no-dev

FROM builder AS app
ARG PG_USERNAME="postgres" \
    PG_PASSWORD="" \
    PG_HOST="localhost" \
    PG_PORT="5432" \
    PG_DATABASE="burplist" \
    DEBUG="false"

ENV PG_USERNAME=${PG_USERNAME} \
    PG_PASSWORD=${PG_PASSWORD} \
    PG_HOST=${PG_HOST} \
    PG_PORT=${PG_PORT} \
    PG_DATABASE=${PG_DATABASE} \
    DEBUG=${DEBUG}

COPY . /app/
CMD ["./docker-entrypoint.sh"]
