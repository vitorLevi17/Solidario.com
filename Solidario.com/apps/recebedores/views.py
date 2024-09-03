from django.shortcuts import render,redirect
from django.utils import timezone
from apps.doacao.forms import DoacaoForm
from apps.recebedores.models import Recebedores


def recebedor_inicio(request):
    return render(request,"recebedor/recebedor_inicio.html")

def recebedor_criar_doacao(request):
    form = DoacaoForm

    if request.method == "POST":
        form = DoacaoForm(request.POST)
        if form.is_valid:
            doacao = form.save(commit=False)
            recebedor = Recebedores.objects.get(user=request.usuario)

            doacao.recebedor = recebedor
            doacao.status_doacao = "Aberto"
            doacao.data_abertura = timezone.now()

            doacao.save()
            return redirect('recebedor_inicio')
    return render(request,"recebedor/recebedor_criar_doacao.html",{'form':form})