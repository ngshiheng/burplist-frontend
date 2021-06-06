<h1 align="center"><strong>Burplist Frontend</strong></h1>

<p align="center">
  <img width=auto height=auto src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
<br />

# What is this?

🇸🇬 A collection of craft beer prices in Singapore.

🖐 Prices of **all** beers in Singapore at your fingertips.

# What is craft beer?

🤤 To simply put, craft beers are the more **delicious** alternative to your mainstream beers.

🍻 In terms of styles, flavours and aroma, craft beers are usually more **diverse** in these aspects.

💁‍♂️ Craft beers are usually brewed in smaller quantities by passionate brewers who care more about **quality** than quantity.

# Development

How to run locally

```
pipenv run python3 app.py --debug=True --port=8080
```

# Deployment

This project is currently hosted on Heroku, proxied by Cloudflare [here](burplist.me)

[Heroku dashboard Link](https://dashboard.heroku.com/apps/burplist-frontend)

```sh
# Print logs for staging
heroku logs --tail --remote staging

# Print logs for production
heroku logs --tail --remote heroku
```
