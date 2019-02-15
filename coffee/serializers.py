from rest_framework import serializers

from .models import Coffee


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = (
            "measured_at",
            "is_powered",
            "started_brewing",
            "temperature",
            "amount",
            "outages",
        )
