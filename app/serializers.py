from rest_framework import serializers
from .models import Sensor_Data

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor_Data
        fields = ['data']