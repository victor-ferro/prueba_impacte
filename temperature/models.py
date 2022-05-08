from django.db import models
from datetime import datetime  

# Create your models here.
class Temperature(models.Model):
    current_temp = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    humidity = models.FloatField()
    name = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)



