from django.urls import path
from .views import recebedor_inicio,recebedor_criar_doacao,aceitar_doacao,recusar_doacao, entregas

urlpatterns = [
    path('recebedor_inicio/',recebedor_inicio,name = 'recebedor_inicio'),
    path('recebedor_criar_doacao/',recebedor_criar_doacao,name = 'recebedor_criar_doacao'),
    path('aceitar_doacao/<int:doacao_id>/',aceitar_doacao,name = 'aceitar_doacao'),
    path('recusar_doacao/<int:doacao_id>/',recusar_doacao,name = 'recusar_doacao'),
    path('entregas/'
         #'<int:doacao_id>''/
         ,entregas,name = 'entregas'),
]