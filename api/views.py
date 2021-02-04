from rest_framework import viewsets
from .permissions import UserPermission
from .models import Ad
from .serializers import AdSerializer
import django_filters.rest_framework


class AdViewset(viewsets.ModelViewSet):
    permission_classes = (UserPermission, )
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['ad_category', 'author']
