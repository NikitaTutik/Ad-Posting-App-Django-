import django_filters
from api.models import *


class AdFilter(django_filters.FilterSet):
    class Meta:
        model = Ad
        fields = ['ad_category']