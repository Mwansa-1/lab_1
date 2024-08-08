from django.shortcuts import render
from .models import Sensor_Data

# restframework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor_Data
from .serializers import SensorDataSerializer
# Create your views here.

def index(request):
    sensor_data = Sensor_Data.objects.all()
    return render(request, 'app/index.html', {'sensor_data': sensor_data})


# API
class SensorDataList(APIView):
    def get(self, request):
        sensor_data = Sensor_Data.objects.all()
        serializer = SensorDataSerializer(sensor_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)