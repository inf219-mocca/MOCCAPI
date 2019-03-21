from rest_framework import serializers

from .models import Coffee


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = '__all__'
