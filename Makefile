dev:
	poetry run python3 app.py --debug=True --port=8080

install:
	poetry install --no-root

lint:
	poetry run flake8 --statistics --show-source

build-dev:
	docker build -t burplist-frontend:dev . \
	--build-arg DEBUG=true \
	--build-arg PG_HOST=172.17.0.1

build-prd:
	docker build -t burplist-frontend:prd . \
    --build-arg PG_USERNAME=${PG_USERNAME} \
    --build-arg PG_PASSWORD=${PG_PASSWORD} \
    --build-arg PG_HOST=${PG_HOST} \
    --build-arg PG_PORT=${PG_PORT} \
    --build-arg PG_DATABASE=${PG_DATABASE}

run-dev:
	docker rm -f burplist-frontend || true
	docker run -d -p 8080:8080 --name burplist-frontend burplist-frontend:dev

run-prd:
	docker rm -f burplist-frontend || true
	docker run -d -p 8080:8080 --name burplist-frontend burplist-frontend:prd
