#!/usr/bin/env bash

echo "Starting moccapi in production environment"
pipenv run python manage.py migrate
pipenv run gunicorn moccapi.wsgi:application --access-logfile - --bind localhost:8000 --workers 3
