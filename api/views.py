from rest_framework import viewsets, serializers, filters
from .permissions import UserPermission
from .models import Ad
from .serializers import AdSerializer
import django_filters.rest_framework


class AdViewset(viewsets.ModelViewSet):
    permission_classes = (UserPermission, )
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter]
    filterset_fields = ['ad_category', 'author']
    search_fields = ['title']
    ordering_fields = ['ad_category']
