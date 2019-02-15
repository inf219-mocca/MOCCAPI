# `moccapi` [![pipeline status](https://gitlab.com/inf219-mocca/moccapi/badges/master/pipeline.svg)](https://gitlab.com/inf219-mocca/moccapi/commits/master)[![coverage report](https://gitlab.com/inf219-mocca/moccapi/badges/master/coverage.svg)](https://gitlab.com/inf219-mocca/moccapi/commits/master) 

Repository containing the API server.

# PyCharm w/Django

To configure everything so that stuff works properly, do the following: 

1. Open settings
2. Go to `Languages and frameworks`
3. Select Django
4. Configure the settings according to the image below
5. ???
6. Profit

![settings](settings.png)

To run the Django application, once you've configured it all you need to do is
select the `Configuration` button in the top right, select `Edit
configurations`, press the `+` sign in the upper left corner, select `Django
Server` and press `OK`. While developing you'll frequently need to run
`managy.py` commands. You'll find this console at `Run manage.py Task...` in the
`Tools` menu.

# Initial setup

Initially, you need to create a migration for each app by specifically running
`makemigrations <app_name>` in the `manage.py` console, but once the initial
migration has been made, you only need to write `makemigrations` to create all
the migrations at once. Currently, we have the following applications configured
in Django:

- `coffee`

# Developing

Once you've run the initial (or subsequent) `makemigrations`, you can update the
database tables by running `migrate`. Next up you should probably import some
fixtures so you have some data to work with, you can do this with `loaddata api`
in the `manage.py` console. Now you can start the application and go to
`localhost:8000/api/v1/coffee/` to view it. For a view of the Swagger
documentation go to `localhost:8000/api/v1/swagger/`.

# Code quality

To ensure that the code meets some standard of quality, we're using Flake8,
Black and isort to maintain a consistent standard. For development, to ensure
that everything is up to date, run the following commands:

- `black .` to format all Python code.
- `isort --recursive .` to sort imports.
- `flake8` to check for style warnings, errors etc.
- `python manage.py test` to run tests.

# Docker

Build with `docker build -t moccapi .` and run with `docker run -itd -p
5432:5432 --rm --name moccapi moccapi`
