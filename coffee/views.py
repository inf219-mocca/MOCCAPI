from rest_framework import viewsets

from .models import API
from .serializers import APISerializer


class APIViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = APISerializer
