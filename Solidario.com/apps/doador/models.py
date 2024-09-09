from django.db import models
from django.contrib.auth.models import User

class Doadores(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nm_doador = models.CharField(max_length=50, null= False, blank= False)
    cpf = models.CharField(max_length=11, null= False, blank= False)
    cep = models.CharField(max_length=8, null= False, blank= False,default='00000000')
    telefone = models.CharField(max_length=13, null= False, blank= False)
    historico_doacoes = models.IntegerField(models.CharField(default=0))
    complemento = models.CharField(max_length=255, null= False, blank= False,default="Rua de trás")
    def __str__(self):
        return self.nm_doador



