from django.shortcuts import render

def doador_incio(request):
    return render(request,"doador/doador_inicio.html")
