#!/usr/bin/env bash

echo "Starting moccapi in production environment"
pipenv run gunicorn moccapi.wsgi:application --access-logfile - --bind 0.0.0.0:8000 --workers 3
