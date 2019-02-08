from django.db import models


class Coffee(models.Model):
    temperature = models.PositiveIntegerField()
    cups = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.cups} ({self.amount}) at {self.temperature}"


class Mocca(models.Model):
    is_powered = models.BooleanField()
    started_brewing = models.DateTimeField("started brewing")
    lost_power = models.BooleanField()
    outages = models.DateTimeField()

    def __str__(self):
        return f"{self.is_powered}"


class API(models.Model):
    time = models.DateTimeField("time pulled")
    coffee = models.OneToOneField(Coffee, on_delete=models.CASCADE)
    mocca = models.OneToOneField(Mocca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.time}"
