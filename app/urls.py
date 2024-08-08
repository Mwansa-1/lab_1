from django.urls import path

from . import views
from .views import SensorDataList

urlpatterns = [
    path('', views.index, name='index'),
    path('sensor-data/', SensorDataList.as_view(), name='sensor-data-list'),
]