from datetime import date

from rest_framework import generics

from .models import Brew
from .serializers import BrewSerializer


class BrewTodayView(generics.ListAPIView):
    """
    Returns a count of how many brews there has been today.
    """

    serializer_class = BrewSerializer

    def get_queryset(self):
        return Brew.objects.filter(started_brewing__date=date.today())


class BrewListView(generics.ListAPIView):
    """
    Returns the 25 latest readings from the sensor.
    """

    queryset = Brew.objects.all()[:25]
    serializer_class = BrewSerializer
