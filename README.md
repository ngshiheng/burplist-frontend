<h1 align="center"><strong>Burplist Frontend</strong></h1>

<p align="center">
  <img width=auto height=auto src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
<br />

# What is this?

A frontend repository for https://burplist.me built using PyWebIO.

We collect online craft beer prices in Singapore and share it with the craft beer lovers here in Singapore.

The site acts as a search engine for craft beers in Singapore, providing craft beer lovers pricing information for their favorite beer.

Say goodbye to browsing 10+ different sites at once to shop for your favorite craft beers.

# Development

## How to install

```sh
pipenv sync
```

## Optional: Environment variables

Check out `/src/settings.py` and configure them accordingly.

## How to run locally

```sh
pipenv run python3 app.py --debug=True --port=8080
# At `http://localhost:8080/`
```

# Deployment

This project is currently hosted on [Heroku](https://www.heroku.com/).

## Useful Heroku commands

```sh
heroku git:remote -a burplist-frontend-staging --staging

# Print logs for staging
heroku logs --tail --remote staging

# Print logs for production
heroku logs --tail --remote heroku
```
