from django.shortcuts import render

def recebedor_inicio(request):
    return render(request,"recebedor/recebedor_inicio.html")
