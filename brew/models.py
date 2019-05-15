from datetime import timedelta
from typing import Union

from django.db import models
from django.utils import timezone
import logging

logger = logging.getLogger('debug')

class Brew(models.Model):
    started_brewing = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime (ISO 8601) when the current brew was started.",
    )
    outages = models.DurationField(
        default=timedelta,
        help_text="Total duration of time when the brewer was without power. Null if no outages was detected.",
    )

    class Meta:
        get_latest_by = "started_brewing"
        ordering = ("-started_brewing",)

    def __str__(self):
        return "ID: {}\nStarted brewing: {}\nOutages: {}".format(
            self.id, self.started_brewing, self.outages
        )

    def update_outage(self):
        from coffee.models import Coffee

        latest_reading = Coffee.objects.latest().measured_at
        diff = timezone.now() - latest_reading
        self.outages += diff


def get_brew(power: int) -> Union[Brew, None]:
    latest = Brew.objects.latest()
    diff = (timezone.now() - latest.started_brewing).total_seconds()
    if diff <= 250:
        return latest

    if power > 1000:
        logger.debug("Creating a new brew")
        return Brew()
    elif power < 100:
        logger.debug("Returning latest brew: " + str(latest))
        return latest
    else:
        return
