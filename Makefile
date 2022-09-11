NAME := burplist-frontend
POETRY := $(shell command -v poetry 2> /dev/null)
DOCKER := $(shell command -v docker 2> /dev/null)

ifdef ENVIRONMENT
	ENVIRONMENT := $(ENVIRONMENT)
else
	ENVIRONMENT := development
	PG_HOST := $(shell docker inspect -f '{{range.NetworkSettings.Networks}}{{.Gateway}}{{end}}' dpostgres)
endif

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Welcome to $(NAME) ($(ENVIRONMENT))"
	@echo "Use 'make <target>' where <target> is one of:"
	@echo ""
	@echo "  dev		start local development server"
	@echo "  install	install packages and prepare environment"
	@echo "  lint		run the code linters"
	@echo "  build		build docker image for $(NAME)"
	@echo "  run		run $(NAME) in docker"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

.PHONY: dev
dev:
	$(POETRY) run python3 app.py --debug=True --port=8080

install:
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install --no-root

.PHONY: lint
lint:
	$(POETRY) run flake8 --statistics --ignore=W503,E501 --show-source

build:
	$(DOCKER) build -t $(NAME) . --build-arg ENVIRONMENT=$(ENVIRONMENT)

.PHONY: run
run:
	$(DOCKER) rm -f $(NAME) || true
	$(DOCKER) run -d -p 8080:8080 -e PG_HOST=$(PG_HOST) -e DEBUG=false --name $(NAME) $(NAME)
