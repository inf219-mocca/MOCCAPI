from collections import Counter
from datetime import timedelta
from typing import Union

from django.db import models


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
    from coffee.models import Coffee, POWER_HEATING, POWER_BREWING, POWER_OFF

    brews = Coffee.objects.all()[:10]
    occurrences = Counter([x.is_powered for x in brews])
    most_frequent = occurrences.most_common(1)[0][0]  # lol

    if power > 1000 and most_frequent == POWER_BREWING:
        return Brew()
    elif power < 1000 and (
        most_frequent == POWER_HEATING or most_frequent == POWER_OFF
    ):
        return Brew.objects.latest()
    else:
        return
