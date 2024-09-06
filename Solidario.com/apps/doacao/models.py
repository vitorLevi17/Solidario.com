from django.db import models
from datetime import datetime
from apps.recebedores.models import Recebedores
from apps.doador.models import Doadores
class Item(models.Model):

    opcoes_item = [
        ("COMIDA","comida"),
        ("ROUPA", "roupa"),
        ("BRINQUEDOS", "brinquedos"),
        ("HIGIENE", "higiene"),
        ("BRINQUEDOS", "brinquedos"),
    ]

    nm_item = models.CharField(max_length=255,blank=False,null=False)
    tp_item = models.CharField(max_length=50, choices=opcoes_item,blank=False)


class Doacao(models.Model):

    urgencias = [
        ("LEVE","leve"),
        ("MEDIA", "media"),
        ("URGENTE", "urgente"),
    ]
    modos_entrega = [
        ("PRESENCIAL","presencial"),
        ("DELIVERY", "delivery"),
    ]

    urgencia = models.CharField(max_length=50,choices=urgencias)
    modo_entrega = models.CharField(max_length=50,choices=modos_entrega)
    status_doacao = models.CharField(max_length=50,default="aberto") #aberto, andamento, finalizado e cancelado
    data_abertura = models.DateTimeField(default=datetime.now)
    quantidade = models.IntegerField(null=False,blank=False)
    recebedor = models.ForeignKey(to=Recebedores,on_delete=models.CASCADE,null=False,blank=False,related_name="recebedor_doacao")
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE,null=False,blank=False,related_name="item_doacao")

class Doacao_Rec(models.Model):

    modos_entrega = [
        ("PRESENCIAL","presencial"),
        ("DELIVERY", "delivery"),
    ]

    modo_entrega = models.CharField(max_length=50,choices=modos_entrega)
    data_recebimento = models.DateTimeField(default=datetime.now)
    doador = models.ForeignKey(to=Doadores,on_delete=models.CASCADE,null=False,blank=False,related_name="doadores")
    doacao_pedido = models.ForeignKey(to=Doacao,on_delete=models.CASCADE,null=False,blank=False,related_name="doacao_pedido")
    item = models.ForeignKey(to=Item,on_delete=models.CASCADE,null=False,blank=False,related_name="item")

