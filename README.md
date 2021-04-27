<h1 align="center"><strong>Burplist Frontend</strong></h1>

<p align="center">
  <img width="300" height="300" src="https://media.giphy.com/media/DGWAx8d3IkICs/giphy.gif">
</p>
<br />

> Collect all the available beers (preferably craft beers 🍻) data in Singapore into a single place so that users can easy compare prices across different vendors and shops.

## MVP Flow

1. User enters a search string, i.e. "Road Hog"
2. Input used as a string for full text search in PostgreSQL via SQLAlchemy
3. Returns the result in table
4. Display it back to the user

## Development

How to run locally

```
pipenv run python3 app.py
```
