from rest_framework import viewsets
from .models import Ad
from .serializers import AdSerializer


class AdViewset(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
