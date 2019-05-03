#!/usr/bin/env bash
export DEBUG=1
while true; do
  echo "Re-starting Django runserver"
  python manage.py runserver
  sleep 2
done
