import random

from celery import shared_task

from brew.models import get_brew
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

    if temp > 200:
        return

    amount = random.uniform(0, 1)
    brew = get_brew(current)
    power = power_status(current)
    coffee = Coffee(brew=brew, temperature=temp, amount=amount, is_powered=power)
    brew.save()
    coffee.save()
