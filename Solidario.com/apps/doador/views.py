from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from apps.doacao.models import Doacao,DoacaoRec
from apps.doacao.forms import DoacaoRecForm
from apps.doador.models import Doadores
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.sistema.api import con_cep

@login_required(login_url='login')
def doador_incio(request):
    doador = Doadores.objects.get(usuario = request.user)
    doa = Doacao.objects.filter(status_doacao = "aberto")
    doa_lem = DoacaoRec.objects.filter(status = "andamento",doador = doador)
    doacoes = []
    for doacao in doa:
        cep = doacao.recebedor.cep
        dados_cep = con_cep(cep)
        doacoes.append({
            'id': doacao.id,
            'item': doacao.item,
            'quantidade': doacao.quantidade,
            'recebedor': doacao.recebedor,
            'urgencia': doacao.get_urgencia_display,
            'modo_entrega': doacao.get_modo_entrega_display,
            'doa':doa,
            'dados_cep':dados_cep
        })

    doacoes_lem = []
    for doacao in doa_lem:
        cep = doacao.doacao_pedido.recebedor.cep
        dados_cep_lem = con_cep(cep)
        doacoes_lem.append({
            'id': doacao.doacao_pedido.id,
            'item': doacao.item,
            'quantidade': doacao.quantidade,
            'recebedor': doacao.doacao_pedido.recebedor,
            'data_combinada': doacao.data_combinada,
            'modo_entrega': doacao.modo_entrega,
            'urgencia': doacao.doacao_pedido.urgencia,
            'dados_cep_lem': dados_cep_lem
        })
    return render(request,"doador/doador_inicio.html",{"doacoes":doacoes,"doacoes_lem":doacoes_lem})

@login_required(login_url='login')
def doar(request,doacao_id):

    doacao = get_object_or_404(Doacao,id=doacao_id)
    form = DoacaoRecForm

    if request.method == 'POST':
        form = DoacaoRecForm(request.POST)
        if form.is_valid():
            doador = Doadores.objects.get(usuario=request.user)
            doacao_rec = form.save(commit=False)

            #validacao data
            if doacao_rec.data_combinada <= timezone.now():
                messages.error(request, "A data combinada não pode ser anterior à data de hoje.")
                return redirect('doar', doacao_id=doacao.id)

            # validacao quantidade
            if not doacao.quantidade >= doacao_rec.quantidade:
                messages.error(request, "A quantidade de itens não pode ser maior que a cadastrada na doação")
                return redirect('doar', doacao_id=doacao.id)

                # validacao quantidade
            if not doacao_rec.quantidade > 0:
                messages.error(request, "A quantidade de itens deve ser maior que 0")
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


