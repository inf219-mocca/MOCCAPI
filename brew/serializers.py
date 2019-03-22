from rest_framework import serializers

from .models import Brew


class BrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brew
        fields = ('started_brewing', 'outages')


