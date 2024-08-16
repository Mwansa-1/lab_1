from django.urls import path

from . import views
from .views import SensorDataList,SensorDataDetail,SensorDataCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('sensor-data/', SensorDataList.as_view(), name='sensor-data-list'),
    path('api/sensor-data/<int:pk>/', SensorDataDetail.as_view(), name='sensor_data_detail'),
    path('api/sensor-data/', SensorDataCreate.as_view(), name='sensor_data_create'),
]