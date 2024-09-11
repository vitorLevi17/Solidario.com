from django.db import models
from django.contrib.auth.models import User

class Recebedores(models.Model):
    usuario = models.OneToOneField(User,on_delete=models.CASCADE)
    nm_recebedor = models.CharField(max_length=255, null=False, blank=False, unique=True)
    cnpj = models.CharField(max_length=14, null=False, blank=False,unique=True)
    cep = models.CharField(max_length=8, null=False, blank=False, default='00000000')
    pix = models.CharField(max_length=255, null=False, blank=False)
    telefone = models.CharField(max_length=13, null=False, blank=False, unique=True)
    complemento = models.CharField(max_length=255,null=False,blank=False,default="Rua de trás")

    def __str__(self):
        return self.nm_recebedor



