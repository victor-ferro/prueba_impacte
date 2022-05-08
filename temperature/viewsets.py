from rest_framework import viewsets

from .models import Temperature
from .serializers import TemperatureSerializer
from rest_framework.decorators import api_view
import requests
from rest_framework.response import Response
from django.forms.models import model_to_dict
from datetime import datetime
from django.utils import timezone

class TemperatureViewSet(viewsets.ModelViewSet):
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

@api_view(['GET'])
def execute_weather(request):
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=39.482369&lon=-0.343578&appid=ace8f5a670de1131acb06239c2ad514f&units=metric", params={})
    temp_data = response.json()

    if response.status_code == 200:
        t1 = Temperature(current_temp=temp_data["main"]["temp"], temp_min=temp_data["main"]["temp_min"], temp_max=temp_data["main"]["temp_max"], humidity=temp_data["main"]["humidity"], name=temp_data["name"])
        t1.save()
       
        return Response(response.json())

@api_view(['GET'])
def latest_temperature(request):
    latest_temp = Temperature.objects.latest('created_at')

    response = {
        'current_temp': latest_temp.current_temp,
        'daily_temp': get_media_temp(),
    }
    return Response(response)



def get_media_temp():
    date_from = timezone.now() - timezone.timedelta(days=1)
    last_day_temps = Temperature.objects.filter(created_at__gte=date_from)
    
    media = 0
    for temp in last_day_temps:
        media += temp.current_temp

    return media / len(last_day_temps)