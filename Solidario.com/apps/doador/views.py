from django.shortcuts import render, get_object_or_404, redirect
from apps.doacao.models import Doacao
from apps.doacao.forms import DoacaoForm,DoacaoRecForm
from apps.doador.models import Doadores

def doador_incio(request):
    doacoes = Doacao.objects.all()
    return render(request,"doador/doador_inicio.html",{"doacoes":doacoes})
def doar(request,doacao_id):
    doacao = get_object_or_404(Doacao,id=doacao_id)
    form = DoacaoRecForm

    if request.method == 'POST':
        form = DoacaoRecForm(request.POST)
        if form.is_valid():
            doador = Doadores.objects.get(usuario=request.user)
            doacao_rec = form.save(commit=False)

            doacao_rec.doacao_pedido = doacao
            doacao_rec.modo_entrega = doacao.modo_entrega
            doacao_rec.item = doacao.item
            doacao_rec.doador = doador
            doacao_rec.save()
            return redirect('doador_inicio')


    return render(request,"doador/doar.html",{'form':form,'doacao':doacao})
