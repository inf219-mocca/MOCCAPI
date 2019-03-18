from rest_framework import generics

from .models import Coffee
from .serializers import CoffeeSerializer


class CoffeeLatestView(generics.RetrieveAPIView):
    """
    Returns the latest readings from the sensor.
    """

    queryset = Coffee.objects.all()
    serializer_class = CoffeeSerializer

    def get_object(self):
        return self.queryset.latest()


class CoffeeListView(generics.ListAPIView):
    """
    Returns the 10 latest readings from the sensor.
    """

    queryset = Coffee.objects.all()[:25]
    serializer_class = CoffeeSerializer
