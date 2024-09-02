from django.contrib import admin
from .models import Item,Doacao_Item,Item_Doacao_Rec,Doacao,Doacao_Rec

class ListItem(admin.ModelAdmin):
    list_display = ("nm_item","tp_item")

class ListDoacaoItem(admin.ModelAdmin):
    list_display = ("quantidade","item")
class ListItem_Doacao_Rec(admin.ModelAdmin):
    list_display = ("quantidade", "Item")
class ListDoacao(admin.ModelAdmin):
    list_display = ("urgencia",
                    "modo_entrega",
                    "status_doacao",
                    "data_abertura",
                    "recebedor",
                    "doacao_item")

admin.site.register(Item,ListItem)
admin.site.register(Doacao_Item,ListDoacaoItem)
admin.site.register(Item_Doacao_Rec,ListItem_Doacao_Rec)
admin.site.register(Doacao,ListDoacao)
admin.site.register(Doacao_Rec)

