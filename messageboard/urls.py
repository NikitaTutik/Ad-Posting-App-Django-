from django.urls import path
from .views import index, add_ad, delete_ad


urlpatterns = [
    path('', index, name='index'),
    path('add/', add_ad, name='add'),
    path('<int:id>/', add_ad, name='update'),
    path('delete/<int:id>/', delete_ad, name='delete')
]

