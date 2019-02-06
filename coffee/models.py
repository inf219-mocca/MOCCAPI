from django.db import models


class Coffee(models.Model):
    temperature = models.PositiveIntegerField()
    cups = models.PositiveSmallIntegerField()
    amount = models.PositiveSmallIntegerField()


class Mocca(models.Model):
    is_powered = models.BooleanField()
    started_brewing = models.DateTimeField("started brewing")
    lost_power = models.BooleanField()
    outages = models.DateTimeField()


class API(models.Model):
    time = models.DateTimeField("time pulled")
    coffee = models.OneToOneField(Coffee, on_delete=models.CASCADE)
    mocca = models.OneToOneField(Mocca, on_delete=models.CASCADE)
