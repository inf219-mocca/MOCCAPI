from django.db import models

from brew.models import Brew

POWER_OFF = 0
POWER_HEATING = 1
POWER_BREWING = 2
POWER_STATUS = (
    (POWER_OFF, "Power off"),
    (POWER_HEATING, "Heating"),
    (POWER_BREWING, "Brewing"),
)


def power_status(current: float) -> int:
    """
    Converts the (power) current into one of the choices used in our Coffee
    model.
    """
    if current >= 1000:
        return POWER_BREWING
    elif 10 < current < 1000:
        return POWER_HEATING
    else:
        return POWER_OFF


class Coffee(models.Model):
    brew = models.ForeignKey(Brew, on_delete=models.CASCADE)
    measured_at = models.DateTimeField(
        help_text="Datetime (ISO 8601) when the data was read."
    )
    temperature = models.FloatField(help_text="Temperature of the coffee")
    amount = models.FloatField(
        help_text="Amount of coffee in the pot, going from 0 (empty) to 1 (full)."
    )
    is_powered = models.PositiveSmallIntegerField(
        choices=POWER_STATUS,
        default=POWER_OFF,
        help_text="""Power status of the coffee machine:
    0. The machine is powered off.
    1. The machine is keeping the coffee hot.
    2. The machine is brewing coffee.""",
    )

    class Meta:
        get_latest_by = "measured_at"
        ordering = ("-measured_at",)

    def __str__(self):
        return f"{self.measured_at}: {self.amount} at {self.temperature}C"
