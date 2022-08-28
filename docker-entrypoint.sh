#!/bin/sh

set -e

exec poetry run python3 app.py --port=8080 "--debug=False", "--port=8080"
