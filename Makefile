install:
	poetry install --no-root

lint:
	poetry run flake8 --statistics --show-source

build:
	docker build -t burplist-frontend .

run:
	poetry run python3 app.py --debug=True --port=8080
