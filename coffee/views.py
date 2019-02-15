from rest_framework import generics

from .models import API
from .serializers import APISerializer


class APILatestView(generics.RetrieveAPIView):
    """
    Returns the latest readings from the sensor.
    """

    queryset = API.objects.all()
    serializer_class = APISerializer

    def get_object(self):
        return self.queryset.latest()


class APIListView(generics.ListAPIView):
    """
    Returns the 10 latest readings from the sensor.
    """

    queryset = API.objects.all()[:10]
    serializer_class = APISerializer
