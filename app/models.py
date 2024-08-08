from django.db import models

# Create your models here.

class Sensor_Data(models.Model):
    data = models.CharField(max_length=100)
