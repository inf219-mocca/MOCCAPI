#!/usr/bin/env bash
while true; do
  echo "Re-starting Django runserver"
  python manage.py runserver
  sleep 2
done
