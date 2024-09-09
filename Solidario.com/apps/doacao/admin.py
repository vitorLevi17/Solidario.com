from django.contrib import admin
from .models import Item,Doacao,DoacaoRec

class ListItem(admin.ModelAdmin):
    list_display = ("nm_item","tp_item")

class ListDoacao(admin.ModelAdmin):
    list_display = ("urgencia",
                    "modo_entrega",
                    "status_doacao",
                    "data_abertura",
                    "recebedor",
                    "item")

admin.site.register(Item,ListItem)
admin.site.register(Doacao,ListDoacao)
admin.site.register(DoacaoRec)

