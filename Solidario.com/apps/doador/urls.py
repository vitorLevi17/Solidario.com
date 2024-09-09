from django.urls import path
from .views import doador_incio,doar

urlpatterns = [
    path('doador_inicio/',doador_incio,name='doador_inicio'),
    path('doar/<int:doacao_id>',doar,name='doar'),
]
