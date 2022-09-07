install:
	poetry install --no-root

lint:
	poetry run flake8 --statistics --show-source

build:
	docker build -t burplist-frontend .

run-docker:
	docker run -d -p 8080:8080 --name burplist-frontend burplist-frontend

run:
	poetry run python3 app.py --debug=True --port=8080
