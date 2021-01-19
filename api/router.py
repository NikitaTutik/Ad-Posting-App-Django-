from rest_framework import routers
from .views import AdViewset

router = routers.DefaultRouter()
router.register('ads', AdViewset)