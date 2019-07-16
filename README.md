# Represent Minnesota
Minnesota based instance of represent-boundaries.

## Installing

1. clone git repo
2. `pipenv install`
3. Copy .env.example to .env and fill in the values

## Running

1. `pipenv shell`
2. `python manage.py loadshapefiles` (use `--reload` to reload the shapefiles)
3. `python manage.py runserver`

## Heroku setup

1. heroku pg:psql
2. ` CREATE EXTENSION postgis;`
3. `python manage.py loadshapefiles` (for our quantity of data, this takes a long time)
4. `exit;`
4. `heroku config:set BUILD_WITH_GEO_LIBRARIES=1` (this potentially takes a long time)

## Docs

https://opennorth.github.io/represent-boundaries-docs/