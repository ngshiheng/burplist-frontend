NAME := burplist-frontend
POETRY := $(shell command -v poetry 2> /dev/null)
DOCKER := $(shell command -v docker 2> /dev/null)

ENVIRONMENT ?= development
PG_HOST := $(shell docker inspect -f '{{range.NetworkSettings.Networks}}{{.Gateway}}{{end}}' dpostgres)

.DEFAULT_GOAL := help

.PHONY: help
help:	## display this help message.
	@echo "Welcome to $(NAME) ($(ENVIRONMENT))!"
	@awk 'BEGIN {FS = ":.*##"; printf "Use make \033[36m<target>\033[0m where \033[36m<target>\033[0m is one of:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: install
install:	## install packages and prepare environment.
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install --no-root

.PHONY: generate
generate:	## export poetry lock file to `requirements.txt`.
	@$(POETRY) export -f requirements.txt --output requirements.txt

.PHONY: lint
lint:	## run the flake8 code linter.
	@$(POETRY) run flake8 --statistics --show-source

.PHONY: build
build:	## build docker image.
	$(DOCKER) build -t $(NAME) . --build-arg ENVIRONMENT=$(ENVIRONMENT) -f docker/Dockerfile

.PHONY: run
run:	## run local development server in docker.
	@$(DOCKER) stop $(NAME) || true && $(DOCKER) rm $(NAME) || true
	$(DOCKER) run -d -p 8080:8080 -e PG_HOST=$(PG_HOST) -e DEBUG=false --name $(NAME) $(NAME)

.PHONY: dev
dev:	## run local development server.
	$(POETRY) run python3 app.py --debug=True --port=8080
