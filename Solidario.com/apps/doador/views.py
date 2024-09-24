from django.shortcuts import render, get_object_or_404, redirect
from apps.doacao.models import Doacao,DoacaoRec
from apps.doacao.forms import DoacaoRecForm
from apps.doador.models import Doadores
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def doador_incio(request):
    doacoes = Doacao.objects.filter(status_doacao = "aberto")
    return render(request,"doador/doador_inicio.html",{"doacoes":doacoes})

@login_required(login_url='login')
def doar(request,doacao_id):

    doacao = get_object_or_404(Doacao,id=doacao_id)
    form = DoacaoRecForm

    if request.method == 'POST':
        form = DoacaoRecForm(request.POST)
        if form.is_valid():
            doador = Doadores.objects.get(usuario=request.user)
            doacao_rec = form.save(commit=False)
            if not doacao.quantidade >= doacao_rec.quantidade:
                messages.error(request, "A quantidade de itens não pode ser maior que a cadastrada na doacao")
                return redirect('doar', doacao_id=doacao.id)


            doacao_rec.doacao_pedido = doacao
            doacao_rec.modo_entrega = doacao.modo_entrega
            doacao_rec.item = doacao.item
            doacao_rec.doador = doador
            doacao_rec.save()
            return redirect('doador_inicio')


    return render(request,"doador/doar.html",{'form':form,'doacao':doacao})
@login_required(login_url='login')
def status_doacoes(request):

    doador = get_object_or_404(Doadores, usuario=request.user)
    doacao_rec = DoacaoRec.objects.filter(doador=doador)  # Corrigido para buscar todas as doações
    return render(request, 'doador/status_doacoes.html', {'doacao_rec': doacao_rec})


