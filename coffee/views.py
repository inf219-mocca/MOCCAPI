from rest_framework import generics

from .models import API
from .serializers import APISerializer


class APIViewSet(generics.ListAPIView):
    queryset = API.objects.all()
    serializer_class = APISerializer
