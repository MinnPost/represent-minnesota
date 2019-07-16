# Represent Minnesota
Minnesota based instance of [Represent Boundaries](https://opennorth.github.io/represent-boundaries-docs/).

## Installing

1. Follow [this documentation](https://opennorth.github.io/represent-boundaries-docs/docs/install/) to setup Python and PostGIS. As of **July 16, 2019**, from this URL you should start by following steps 1-7 under Install Dependencies, and then step 1 under Install Represent Boundaries.
2. Clone this git repository.
3. Run `pipenv install`. This completes steps 2-6 of the Install Represent Boundaries section of the docs above.
4. Copy .env.example to .env and fill in the values from your local setup (or Heroku if you are deploying). This veers away from the docs above for the sake of hosting on Heroku more easily.
5. Run `python manage.py migrate` to initially populate the database.

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
