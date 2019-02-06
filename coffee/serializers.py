from rest_framework import serializers
from .models import API


class APISerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = API
        fields = ("time", "coffee", "mocca")
