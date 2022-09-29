# Represent Minnesota
Minnesota based instance of [Represent Boundaries](https://opennorth.github.io/represent-boundaries-docs/).

## Installing

1. Follow [this documentation](https://opennorth.github.io/represent-boundaries-docs/docs/install/) to setup Python and PostGIS. As of **July 16, 2019**, from this URL you should start by following steps 1-7 under Install Dependencies, and then step 1 under Install Represent Boundaries.
2. Clone this git repository.
3. Run `pipenv install`. This completes steps 2-6 of the Install Represent Boundaries section of the docs above.
4. Copy .env.example to .env and fill in the values from your local setup (or Heroku if you are deploying). This veers away from the docs above for the sake of hosting on Heroku more easily. `SECRET_KEY` cannot be blank.
5. Run `python manage.py migrate` to initially populate the database.

## Running

1. `pipenv shell`
2. `python manage.py loadshapefiles` (use `--reload` to reload the shapefiles)
3. `python manage.py runserver`

## Heroku setup

1. Run `heroku pg:psql` to log in to your Heroku Postgres database.
2. Run `CREATE EXTENSION postgis;` to install the PostGIS extension to Postgres.
3. Run `exit;` to get out of Postgres.
4. Run `heroku config:set BUILD_WITH_GEO_LIBRARIES=1` to instruct Heroku to build with geo libraries (this potentially takes a long time). Otherwise you'll run into issues when you try the next step.
5. Run `python manage.py loadshapefiles` to populate the data Represent Boundaries will use (for our quantity of data, this takes a long time).

## Installing new boundaries

1. Find the dataset. If it's a redistricting of an existing boundary, you can often find it at the same place, with changing the URL for the year.
1. Download the shapefiles and put them into a subfolder under `data/shapefiles`. Update `data/shapefiles/definitions.py` to match the new file path and whatever information you have from the source.
1. With updated files, things like `name_func`, `id_func`, and `slug_func` will sometimes need new parameters. Sometimes this information is available in metadata for the new set.
1. After pushing to Heroku with the new shapefiles, follow the steps below for running on Heroku.

### When redistricting happens

It can be hard to find updated data sources. The state may release a Redistricting boundary set, like [this one from 2020](https://gisdata.mn.gov/dataset/society-redistricting-2020), which "includes MN Secretary of State election data from 2012-2020 that was disaggregated to census block level and aggregated to voting districts, minor civil divisions and counties." In this case, it's possible to separate census blocks, counties, minor civil divisions, and voting districts and run them within separate folders.

## Running on Heroku

1. Deploy production code to Heroku by running `git push heroku master`. The production version deploys to https://represent-minnesota.herokuapp.com/.
1. Deploy staging code to Heroku by pushing to the `staging` branch of this repository. This verison deploys at https://represent-minnesota-staging.herokuapp.com/.
1. To update the shapefiles in the Heroku database, run `heroku run python manage.py loadshapefiles --reload` (use `--reload` to reload the shapefiles). Currently this should only happen with the full dataset in production and not staging, since the set is too big for the free database plan.

## Working with Django admin

1. It can be useful to have a login for the Django admin. To create one locally, run `python manage.py createsuperuser`. To do it on Heroku, run `heroku run python manage.py createsuperuser --app represent-minnesota`.
2. Boundaries and boundary sets can both be modified via the Django admin.
