#!/bin/sh

set -e

poetry run python3 app.py --debug="${DEBUG}"

exec "$@"
