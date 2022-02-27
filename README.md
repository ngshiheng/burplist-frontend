<h1 align="center"><strong>Burplist Frontend</strong></h1>

<p align="center">
  <img width=auto height=auto src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
<br />

# What is this?

A frontend repository for https://app.burplist.me built using [PyWebIO](https://github.com/pywebio/PyWebIO).

The site serves as a search engine for craft beers in Singapore, providing craft beer lovers pricing information for their favorite beer.

I have documented some of my thought process and engineering decisions while creating Burplist [here](https://jerrynsh.com/how-i-built-burplist-for-free/). Enjoy!

# Development

## Requirements

-   [Python](https://www.python.org/) 3.9+
-   [poetry](https://python-poetry.org/docs/)
-   [PostgreSQL](https://www.postgresql.org/)

## Database

-   Make sure you have a running instance of the latest PostgreSQL in your local machine
-   Example to spin up a PostgreSQL Docker instance locally

    ```sh
    docker run -d --name dpostgres -p 5432:5432 -e POSTGRES_HOST_AUTH_METHOD=trust postgres:latest
    ```

-   Create a new database name as `burplist`
-   Ensure that `pg_trgm` is installed as your PostgreSQL extension

    ```sql
    CREATE EXTENSION pg_trgm;
    ```

## How to install

```sh
poetry install

# Installing dependencies only
poetry install --no-root

# Updating dependencies to their latest versions
poetry update
```

## Setup Pre-commit Hooks

Before you begin your development work, make sure you have installed [pre-commit hooks](https://pre-commit.com/index.html#installation).

Some example useful invocations:

-   `pre-commit install`: Default invocation. Installs the pre-commit script alongside any existing git hooks.
-   `pre-commit install --install-hooks --overwrite`: Idempotently replaces existing git hook scripts with pre-commit, and also installs hook environments.

## Optional: Environment variables

Check out `/src/settings.py` and configure them accordingly.

# Usage

## How to run locally

```sh
poetry run python3 app.py --debug=True --port=8080
# At `http://localhost:8080/`
```

## Start your database

You'll need to setup your Postgres locally based on the instructions [here](https://github.com/ngshiheng/burplist/#database). And then run:

```sh
docker start dpostgres
```

## Optional: Using Docker

```sh
# Build the Docker image
docker build -t burplist-frontend .

# Run the image in a container
docker run -d -p 8080:8080 --name burplist-frontend burplist-frontend

# Go to localhost:8080 and DONE!
```

# Deployment

This project is currently hosted on [Heroku](https://www.heroku.com/).

## Optional: Useful Heroku commands

```sh
heroku git:remote -a burplist-frontend-staging --staging

# Print logs for staging
heroku logs --tail --remote staging

# Print logs for production
heroku logs --tail --remote heroku
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### Steps

1. Fork this
2. Create your feature branch (`git checkout -b jimmy/fooBar`)
3. Commit your changes (`git commit -am 'feat: add some fooBar'`, make sure that your commits are [semantic](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716))
4. Push to the branch (`git push origin jimmy/fooBar`)
5. Create a new Pull Request
