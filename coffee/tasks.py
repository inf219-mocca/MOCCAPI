import random
import statistics

from celery import shared_task

from brew.models import get_brew
from sensors.arduino import Arduino

from .models import POWER_BREWING, Coffee, power_status


def valid_reading(temp: int, power: int) -> bool:
    if temp >= 200:
        return False

    latest_readings = Coffee.objects.all()[:10]
    average_temp = statistics.mean([x.temperature for x in latest_readings])
    diff = abs(average_temp - temp)

    if diff >= 20 and power != POWER_BREWING:
        return False

    return True


@shared_task()
def insert_coffee():
    """
    Used by Celery to asynchronously query the Arduino, read the latest
    reading from it and create a new Coffee model and save it.
    """
    a = Arduino()
    current, temp = a.read()
    power = power_status(current)

    if not valid_reading(temp, power):
        return

    amount = random.uniform(0, 1)
    brew = get_brew(current)

    if brew is None:
        return

    coffee = Coffee(
        brew=brew, temperature=temp, amount=amount, status=power, power=current
    )
    brew.save()
    coffee.save()
