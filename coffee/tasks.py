import statistics

from celery import shared_task

from brew.models import get_brew
from sensors.arduino import Arduino
from sensors.camera import convert_image, take_picture
from sensors.liquid import calculate_liquid

from .models import POWER_BREWING, Coffee, power_status

HEIGHT = 360
WIDTH = 640
THRESHOLD = 80
MEAN = 0.5


def valid_reading(temp: int, power: int) -> bool:
    """Heuristics that check whether or not a reading is valid or not."""
    if temp >= 200:
        return False

    latest_readings = Coffee.objects.all()[:10]
    average_temp = statistics.mean([x.temperature for x in latest_readings])
    diff = abs(average_temp - temp)

    if diff >= 20 and power != POWER_BREWING:
        return False

    return True


@shared_task()
def event_loop():
    """
    Used by Celery to asynchronously query the Arduino, read the latest
    reading from it and create a new Coffee model and save it.
    """
    a = Arduino()
    current, temp = a.read()
    power = power_status(current)

    if not valid_reading(temp, power):
        return False

    image = take_picture(WIDTH, HEIGHT)
    img_array = convert_image(image, THRESHOLD, MEAN)
    amount = calculate_liquid(img_array, HEIGHT)
    brew = get_brew(current)

    if brew is None:
        return False

    if power == 0:
        brew.update_outage()

    coffee = Coffee(
        brew=brew, temperature=temp, amount=amount, status=power, current=current
    )
    brew.save()
    coffee.save()

    return True
