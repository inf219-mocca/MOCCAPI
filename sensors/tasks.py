from __future__ import absolute_import, unicode_literals

from celery import shared_task
from serial import Serial


@shared_task
def read(arduino: str) -> (float, float):
    """
    Does a single read on the serial interface to the Arduino reading the
    current power and temperature.
    :return: (current, temp)
    """
    with Serial(arduino) as ser:
        read_arduino = ser.readline().decode("utf-8").strip()
        current, temp = read_arduino.split("\t")
    return current, temp
