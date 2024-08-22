from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.sistema.urls')),
    #path('',include('apps.doador.urls')),
    #path('',include('apps.recebedores.urls'))
]
