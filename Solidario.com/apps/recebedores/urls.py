from django.urls import path
from .views import *

urlpatterns = [
    path('recebedor_inicio/',recebedor_inicio,name = 'recebedor_inicio'),
    path('recebedor_criar_doacao/',recebedor_criar_doacao,name = 'recebedor_criar_doacao'),
    path('aceitar_doacao/<int:doacao_id>/',aceitar_doacao,name = 'aceitar_doacao'),
    path('recusar_doacao/<int:doacao_id>/',recusar_doacao,name = 'recusar_doacao'),
    path('entregas/',entregas,name = 'entregas'),
    path('receber_doacao/',receber_doacao,name='receber_doacao'),
    path('confirmar_recebimento/<int:recebimento_id>/', confirmar_recebimento, name='confirmar_recebimento'),

]