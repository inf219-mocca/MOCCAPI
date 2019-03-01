import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moccapi.settings")
app = Celery("moccapi")

app.config_from_object("django.conf:settings", namespace="CELERY")
