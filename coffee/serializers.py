from rest_framework import serializers
from .models import API, Coffee, Mocca


class CoffeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coffee
        fields = "__all__"


class MoccaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mocca
        fields = "__all__"


class APISerializer(serializers.HyperlinkedModelSerializer):
    coffee = CoffeeSerializer
    mocca = MoccaSerializer

    class Meta:
        model = API
        fields = ("time", "coffee", "mocca")
