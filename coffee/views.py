from rest_framework import generics

from .models import API
from .serializers import APISerializer


class APIViewSet(generics.RetrieveAPIView):
    queryset = API.objects.all()
    serializer_class = APISerializer

    def get_object(self):
        return self.queryset.latest()
