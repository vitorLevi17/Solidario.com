from django.urls import path
from .views import index,login,cadastro,logout,cadastro_recebedor


urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('cadastro/',cadastro,name='cadastro'),
    path('cadastro_recebedor/',cadastro_recebedor,name='cadastro_recebedor'),
    path('logout/',logout,name='logout')
]
