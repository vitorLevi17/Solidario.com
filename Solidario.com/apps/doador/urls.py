from django.urls import path
from .views import doador_incio

urlpatterns = [
    path('doador_inicio/',doador_incio,name='doador_inicio')
]
