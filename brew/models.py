from django.db import models


class Brew(models.Model):
    started_brewing = models.DateTimeField(
        help_text="Datetime (ISO 8601) when the current brew was started."
    )
    outages = models.DurationField(
        blank=True,
        null=True,
        help_text="Total duration of time when the brewer was without power. Null if no outages was detected.",
    )
