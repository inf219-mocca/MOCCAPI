import random
from datetime import timedelta

from django.utils import timezone

from celery import shared_task

from sensors.arduino import Arduino

from .models import Coffee, power_status


@shared_task()
def insert_coffee():
    """
    Used by Celery to asynchronously query the Arduino, read the latest
    reading from it and create a new Coffee model and save it.
    """
    a = Arduino()
    current, temp = a.read()
    time = timezone.now()
    time_since = random.randint(0, 4)
    started = time - timedelta(hours=time_since)
    amount = random.uniform(0, 1)
    coffee = Coffee(
        measured_at=time,
        temperature=temp,
        amount=amount,
        started_brewing=started,
        is_powered=power_status(current),
    )
    coffee.save()
    print(
        f"\nCurrent: {current}\nTemp: {temp}\nAmount: {amount}\nPower: {coffee.is_powered}\n"
    )
