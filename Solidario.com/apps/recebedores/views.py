from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from apps.doacao.forms import DoacaoForm,DoacaoRecForm
from apps.recebedores.models import Recebedores
from apps.doacao.models import DoacaoRec,Doacao
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def recebedor_inicio(request):
    recebedor = Recebedores.objects.get(usuario = request.user)
    doacoes = DoacaoRec.objects.filter(doacao_pedido__recebedor = recebedor,status="aberto")
    return render(request,"recebedor/recebedor_inicio.html",{'doacoes':doacoes})


@login_required(login_url='login')
def recebedor_criar_doacao(request):
    form = DoacaoForm

    if request.method == "POST":
        form = DoacaoForm(request.POST)
        if form.is_valid:
            doacao = form.save(commit=False)
            recebedor = Recebedores.objects.get(usuario=request.user)

            doacao.recebedor = recebedor
            doacao.data_abertura = timezone.now()

            doacao.save()
            return redirect('recebedor_inicio')
    return render(request,"recebedor/recebedor_criar_doacao.html",{'form':form})


@login_required(login_url='login')
def aceitar_doacao(request, doacao_id):
        doacao_rec = get_object_or_404(DoacaoRec, id=doacao_id)
        form = DoacaoRecForm(instance=doacao_rec)

        if request.method == 'POST':
            form = DoacaoRecForm(request.POST, instance=doacao_rec)
            if form.is_valid():
                doacao_rec = form.save(commit=False)
                doacao_rec.status = "andamento"
                doacao_rec.save()
                return redirect('recebedor_inicio')

        return render(request, 'recebedor/aceitar_doacao.html', {'form':form,'doacao': doacao_rec})


@login_required(login_url='login')
def recusar_doacao(request, doacao_id):
    doacao_rec = get_object_or_404(DoacaoRec,id=doacao_id)

    if request.method == 'POST':
            doacao_rec.status = "cancelado"
            doacao_rec.save()
            return redirect('recebedor_inicio')

    return render(request,'recebedor/recusar_doacao.html',{'doacao':doacao_rec})


@login_required(login_url='login')
def receber_doacao(request):
    recebedor = Recebedores.objects.get(usuario=request.user)
    doacoes = Doacao.objects.filter(recebedor=recebedor,status_doacao='aberto')
    return render(request, 'recebedor/receber_doacao.html', {'doacoes':doacoes})


@login_required(login_url='login')
def ver_doacao(request):
    recebedor = Recebedores.objects.get(usuario = request.user)
    doacoes = Doacao.objects.filter(recebedor=recebedor)
    return render(request,'recebedor/ver_doacao.html',{'doacoes':doacoes})


@login_required(login_url='login')
def confirmar_recebimento(request, recebimento_id):
    recebimento = get_object_or_404(DoacaoRec, id=recebimento_id,status='andamento')

    if recebimento.status == "andamento":

        recebimento.doador.historico_doacoes +=1
        recebimento.status = "finalizado"
        recebimento.data_rec = timezone.now()
        recebimento.save()

        messages.success(request, 'Recebimento confirmado com sucesso!')
    else:
        messages.error(request, 'Este recebimento já foi finalizado.')

    return redirect('receber_doacao')


@login_required(login_url='login')
def finalizar_pedido_doacao(request,doacao_id):
    doacao = get_object_or_404(Doacao,id=doacao_id,status_doacao = "aberto")

    doacao.status_doacao = "finalizado"
    doacao.save()
    messages.success(request,"Seu pedido de doacao foi finalizado")
    return redirect('receber_doacao')


@login_required(login_url='login')
def cancelar_pedido_doacao(request,doacao_id):
    doacao = get_object_or_404(Doacao, id=doacao_id, status_doacao="aberto")

    doacao.status_doacao = "cancelado"
    doacao.save()
    messages.success(request, "Seu pedido de doacao foi cancelado")
    return redirect('receber_doacao')



