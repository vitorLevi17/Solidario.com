from django.urls import path
from .views import recebedor_inicio

urlpatterns = [
    path('recebedor_inicio/',recebedor_inicio,name = 'recebedor_inicio'),
]