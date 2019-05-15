import logging
from typing import Union

import serial.tools.list_ports
from serial import Serial

from moccapi.settings import ARDUINO_ID

logger = logging.getLogger("debug")


class Arduino:
    def __init__(self, timeout: int = 1000):
        self.arduino = self.find_arduino()
        self.timeout = timeout

    @staticmethod
    def find_arduino() -> Union[str, None]:
        """
        Listens on all serial interfaces for our Arduino.
        :return: The serial interface.
        """
        ports = list(serial.tools.list_ports.comports())
        for port in ports:
            if ARDUINO_ID in port.hwid:
                return port.device

    def read(self) -> (float, float):
        """
        Does a single read on the serial interface to the Arduino reading the
        current power and temperature.
        :return: (current, temp)
        """
        ser = Serial(self.arduino)
        ser.write(b"1")
        read = ser.readline().decode("utf-8").strip()
        current, temp = map(float, read.split("\t"))
        logger.debug("Current is: " + str(current) + ", temperature is: " + str(temp))
        return current, temp
