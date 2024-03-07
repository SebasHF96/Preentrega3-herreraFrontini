from django.urls import path
from MedicApp.views import *

urlpatterns = [
    path('', inicio),
    path('alta_profesionales/', profesional),
    path('alta_pacientes/', paciente),
    path('alta_sanatorios/', sanatorio),
    path('buscar_profesional/', buscar_profesional),
    path('resultados/', resultado_profesional),
]
