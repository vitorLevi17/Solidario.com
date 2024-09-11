from django.urls import path
from .views import doador_incio,doar,status_doacoes

urlpatterns = [
    path('doador_inicio/',doador_incio,name='doador_inicio'),
    path('doar/<int:doacao_id>',doar,name='doar'),
    path('status_doacoes/',status_doacoes,name='status_doacoes'),
]
