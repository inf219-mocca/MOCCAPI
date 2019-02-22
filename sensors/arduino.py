from typing import Union

import serial.tools.list_ports
from serial import Serial

# from coffee import models


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
            if "VID:PID=1A86:7523" in port.hwid:
                return port.device

    def read(self) -> (float, float):
        """
        Does a single read on the serial interface to the Arduino reading the
        current power and temperature.
        :return: (current, temp)
        """
        with Serial(self.arduino) as ser:
            read = ser.readline().decode("utf-8").strip()
            current, temp = read.split("\t")
        return current, temp
