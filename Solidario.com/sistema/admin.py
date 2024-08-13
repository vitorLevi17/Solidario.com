from django.contrib import admin
from .models import Doador,CustomUser,Instituicao

admin.site.register(CustomUser)
admin.site.register(Doador)
admin.site.register(Instituicao)
