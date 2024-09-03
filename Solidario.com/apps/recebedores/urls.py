from django.urls import path
from .views import recebedor_inicio,recebedor_criar_doacao

urlpatterns = [
    path('recebedor_inicio/',recebedor_inicio,name = 'recebedor_inicio'),
    path('recebedor_criar_doacao/',recebedor_criar_doacao,name = 'recebedor_criar_doacao'),
]