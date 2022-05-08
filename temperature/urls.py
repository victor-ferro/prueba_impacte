from rest_framework import routers
from .viewsets import TemperatureViewSet

from django.urls import path 
from temperature import viewsets

router = routers.SimpleRouter()
router.register('temperatures', TemperatureViewSet)

urlpatterns = [
    path('execute/', viewsets.execute_weather),
    path('temperatures/latest', viewsets.latest_temperature),
]

urlpatterns += router.urls
