from django.contrib import admin
from apps.doador.models import Doadores

class ListDoa(admin.ModelAdmin):
    list_display = ("usuario","nm_doador","cpf","cep")
    list_display_links = ("usuario","nm_doador")
    search_fields = ("nm_doador",)
    list_per_page = 10

# Register your models here.
admin.site.register(Doadores,ListDoa)
