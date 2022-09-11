NAME := burplist-frontend
POETRY := $(shell command -v poetry 2> /dev/null)
PG_HOST := $(shell docker inspect -f '{{range.NetworkSettings.Networks}}{{.Gateway}}{{end}}' dpostgres)

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Use 'make <target>' where <target> is one of:"
	@echo ""
	@echo "  dev		start development server"
	@echo "  install	install packages and prepare environment"
	@echo "  lint		run the code linters"
	@echo "  build-dev	build dev docker image for $(NAME)"
	@echo "  build-prd	build prd docker image for $(NAME)"
	@echo "  run-dev	run $(NAME) in dev docker"
	@echo "  run-prd	run $(NAME) in prd docker"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

.PHONY: dev
dev:
	poetry run python3 app.py --debug=True --port=8080

install:
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	$(POETRY) install --no-root

.PHONY: lint
lint:
	$(POETRY) run flake8 --statistics --ignore=W503,E501 --show-source

build-dev:
	docker build -t $(NAME):dev . \
	--build-arg DEBUG=true \
	--build-arg PG_HOST=172.17.0.1

build-prd:
	docker build -t $(NAME):prd . \
    --build-arg PG_USERNAME=${PG_USERNAME} \
    --build-arg PG_PASSWORD=${PG_PASSWORD} \
    --build-arg PG_HOST=${PG_HOST} \
    --build-arg PG_PORT=${PG_PORT} \
    --build-arg PG_DATABASE=${PG_DATABASE}

.PHONY: run-dev
run-dev:
	docker rm -f $(NAME) || true
	docker run -d -p 8080:8080 --name $(NAME) $(NAME):dev

.PHONY: run-prd
run-prd:
	docker rm -f $(NAME) || true
	docker run -d -p 8080:8080 --name $(NAME) $(NAME):prd
