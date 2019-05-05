# `moccapi` [![CircleCI](https://circleci.com/gh/inf219-mocca/MOCCAPI.svg?style=svg)](https://circleci.com/gh/inf219-mocca/MOCCAPI) [![codecov](https://codecov.io/gh/inf219-mocca/MOCCAPI/branch/master/graph/badge.svg)](https://codecov.io/gh/inf219-mocca/MOCCAPI)

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
select the `Configuration` button in the top right, select `Edit configurations`, press the `+` sign in the upper left corner, select `Django Server` and press `OK`. While developing you'll frequently need to run
`managy.py` commands. You'll find this console at `Run manage.py Task...` in the
`Tools` menu.

# Initial setup

Initially, you need to create a migration for each app by specifically running
`makemigrations <app_name>` in the `manage.py` console, but once the initial
migration has been made, you only need to write `makemigrations` to create all
the migrations at once. Currently, we have the following applications configured
in Django:

- `brew`
- `coffee`
- `django_celery_results` (used for async storing of results)

# Developing

**NOTE:** You need to tell the Django instance that is in debug mode, the easiest
way to run the server is with the `devserver.sh` file, or by setting the
environment variable `DEBUG` to `1`. On any unix system you do this by writing
`export DEBUG=1` in your terminal, or you could configure it from your settings
inside PyCharm.

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

# Reading from the Arduino

There is a separate application for reading from the Arduino in the `sensors`
folder, if you want to read some data from the Arduino you can run it from a
terminal and get a single reading from the sensors.

```python
from sensors.arduino import Arduino
arduino = Arduino()
```

And then read from the Arduino.

```python
arduino.read()
# ('2122.39', '26.31')
```

# Using Celery

We are using Celery for asynchronously being able to query the Arduino and add
the results to the database. For this you need to have RabbitMQ installed as it
is our broker, then to actually run Celery and RabbitMQ you need to run the
following two commands in two separate terminal windows:

1. `rabbitmq-server`
2. `celery -A moccapi worker -l info -B`

While you are running the application you'll see the results of the asynchronous
queries that are run every few seconds in the `celery` terminal window:

```shell
[2019-03-01 11:57:15,566: INFO/MainProcess] Received task: sensors.tasks.read[58b27a8f-1e9d-4bb2-9118-b4896be2ed3f]
[2019-03-01 11:57:17,394: INFO/ForkPoolWorker-8] Task sensors.tasks.read[58b27a8f-1e9d-4bb2-9118-b4896be2ed3f] succeeded in 1.8236205450000043s: ('2111.73', '23.27')
```
