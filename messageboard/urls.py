from django.urls import path
from .views import index, add_ad, delete_ad, pin_ad, unpin_ad


urlpatterns = [
    path('', index, name='index'),
    path('add/', add_ad, name='add'),
    path('<int:id>/', add_ad, name='update'),
    path('delete/<int:id>/', delete_ad, name='delete'),
    path('<int:pk>/pin', pin_ad, name='pin'),
    path('<int:pk>/unpin', unpin_ad, name='unpin'),
]

