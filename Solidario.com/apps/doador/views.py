from django.shortcuts import render
from apps.doacao.models import Doacao

def doador_incio(request):
    doacoes = Doacao.objects.all()
    return render(request,"doador/doador_inicio.html",{"doacoes":doacoes})
