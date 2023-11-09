from django.contrib import admin
from django.urls import path

from Automovil.views import (
    listar_Auto, listar_Alquiler, listar_Conductor
)

urlpatterns = [
    path('Auto/', listar_Auto),
    path('Alquiler/', listar_Alquiler),
    path('Conductor/', listar_Conductor),

]