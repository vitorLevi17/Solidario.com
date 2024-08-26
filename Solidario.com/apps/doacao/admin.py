from django.contrib import admin
from .models import Item,Doacao_Item,Item_Doacao_Rec,Doacao,Doacao_Rec

admin.site.register(Item)
admin.site.register(Doacao_Item)
admin.site.register(Item_Doacao_Rec)
admin.site.register(Doacao)
admin.site.register(Doacao_Rec)

