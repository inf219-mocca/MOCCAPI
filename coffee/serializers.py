from rest_framework import serializers

from .models import Coffee


class CoffeeSerializer(serializers.ModelSerializer):
    brew_started = serializers.DateTimeField(source="brew.started_brewing")
    brew_outages = serializers.DurationField(source="brew.outages")

    class Meta:
        model = Coffee
        fields = (
            "id",
            "measured_at",
            "temperature",
            "amount",
            "status",
            "brew_started",
            "brew_outages",
        )
