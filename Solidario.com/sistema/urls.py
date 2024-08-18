from django.urls import path
from .views import index,login,cadastro,doador_index


urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('cadastro/',cadastro,name='cadastro'),
    path('index_doador/',doador_index,name = 'doador_index')
]
