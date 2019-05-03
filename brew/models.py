from datetime import timedelta
from typing import Union

from django.db import models
from django.utils import timezone


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
        return f"ID: {self.id}\nStarted brewing: {self.started_brewing}\nOutages: {self.outages}"


def get_brew(power: int) -> Union[Brew, None]:
    latest = Brew.objects.latest()
    diff = (latest.started_brewing - timezone.now()).total_seconds()
    if diff <= 250:
        return latest

    if power > 1000:
        return Brew()
    elif power < 100:
        return latest
    else:
        return
