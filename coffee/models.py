from django.db import models


class Coffee(models.Model):
    POWER_OFF = 0
    POWER_HEATING = 1
    POWER_BREWING = 2
    POWER_STATUS = (
        (POWER_OFF, "Power off"),
        (POWER_HEATING, "Heating"),
        (POWER_BREWING, "Brewing"),
    )
    time = models.DateTimeField("time pulled")
    temperature = models.FloatField()
    amount = models.FloatField()
    is_powered = models.PositiveSmallIntegerField(
        choices=POWER_STATUS,
        default=POWER_OFF,
        help_text="""Power status of the coffee machine:
    0. The machine is powered off.
    1. The machine is keeping the coffee hot.
    2. The machine is brewing coffee.""",
    )
    started_brewing = models.DateTimeField("started brewing")
    outages = models.DurationField(blank=True, null=True)

    class Meta:
        get_latest_by = "time"

    def __str__(self):
        return f"{self.time}: {self.amount} at {self.temperature}C"
