from django.db import models


class Brew(models.Model):
    started_brewing = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime (ISO 8601) when the current brew was started.",
    )
    outages = models.DurationField(
        help_text="Total duration of time when the brewer was without power. Null if no outages was detected."
    )

    class Meta:
        get_latest_by = "started_brewing"
        ordering = ("-started_brewing",)

    def __str__(self):
        return f"ID: {self.id}\nStarted brewing: {self.started_brewing}\nOutages: {self.outages}"


def get_brew(power: int) -> Brew:
    from coffee.models import Coffee

    if power > 1000:
        return Brew.objects.latest()
    elif power < 1000 and Coffee.objects.latest().is_powered > 2:
        return Brew()
    else:
        raise Exception("This shouldn't happen...")
