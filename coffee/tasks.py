import random
from datetime import timedelta

from django.utils import timezone

from celery import shared_task

from sensors.arduino import Arduino

from .models import Coffee


@shared_task()
def insert_coffee():
    """worst code ever"""
    a = Arduino()
    current, temp = a.read()
    time = timezone.now()
    time_since = random.randint(0, 4)
    started = time - timedelta(hours=time_since)
    amount = random.uniform(0, 1)
    coffee = Coffee(
        measured_at=time, temperature=temp, amount=amount, started_brewing=started
    )
    coffee.save()
    coffee.power_status(float(current))
    print(f"\nCurrent: {current}\nTemp: {temp}\nAmount: {amount}\n")
    return True
