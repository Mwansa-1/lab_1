from django.db import models

# Create your models here.

class Sensor_Data(models.Model):
    temperature = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
