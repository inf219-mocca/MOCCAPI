from rest_framework import viewsets
from .serializers import APISerializer
from .models import API


class APIViewSet(viewsets.ModelViewSet):
    queryset = API.objects.all()
    serializer_class = APISerializer
