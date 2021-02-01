from rest_framework import viewsets
from .models import Ad
from .serializers import AdSerializer
import django_filters.rest_framework


class AdViewset(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['ad_category', 'author']
