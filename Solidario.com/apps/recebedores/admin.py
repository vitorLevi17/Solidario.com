from django.contrib import admin
from apps.recebedores.models import Recebedores

class ListRecebedor(admin.ModelAdmin):
    list_display = ("usuario", "nm_recebedor","pix")
    list_display_links = ("usuario","nm_recebedor")


admin.site.register(Recebedores,ListRecebedor)
