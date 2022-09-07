ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION}-slim AS base
ARG DEBUG=false \
    PG_HOST=172.17.0.1
ENV DEBUG=${DEBUG} \
    PG_HOST=${PG_HOST} \
    PYTHONUNBUFFERED=1 \
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
RUN poetry install --no-root

FROM builder AS app
COPY . /app/
CMD ["./docker-entrypoint.sh"]
