from django.db import models


class Coffee(models.Model):
    time = models.DateTimeField("time pulled")
    temperature = models.FloatField()
    amount = models.FloatField()
    is_powered = models.BooleanField()
    started_brewing = models.DateTimeField("started brewing")
    outages = models.DurationField(blank=True, null=True)

    class Meta:
        get_latest_by = "time"

    def __str__(self):
        return f"{self.time}: {self.amount} at {self.temperature}C"
