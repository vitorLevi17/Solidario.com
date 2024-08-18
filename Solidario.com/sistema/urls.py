from django.urls import path
from .views import index,login,cadastro


urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('cadastro/',cadastro,name='cadastro'),
]
