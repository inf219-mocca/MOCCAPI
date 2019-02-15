from rest_framework import serializers

from .models import API, Coffee, Mocca


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = ("temperature", "amount")


class MoccaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mocca
        fields = ("is_powered", "started_brewing", "outages")


class APISerializer(serializers.ModelSerializer):
    coffee = CoffeeSerializer(many=False, read_only=True)
    mocca = MoccaSerializer(many=False, read_only=True)

    class Meta:
        model = API
        fields = ("time", "coffee", "mocca")
