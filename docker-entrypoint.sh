#!/bin/sh

set -e

exec poetry run python3 app.py --debug="${DEBUG}"
