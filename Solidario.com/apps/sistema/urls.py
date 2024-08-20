from django.urls import path
from .views import index,login,cadastro,logout


urlpatterns = [
    path('',index,name='index'),
    path('login/',login,name='login'),
    path('cadastro/',cadastro,name='cadastro'),
    path('logout/',logout,name='logout')
]
