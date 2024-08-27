from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('agendar/', views.agendar_servico, name='agendar'),
    path('confirmacao/', views.confirmacao, name='confirmacao'),
]
