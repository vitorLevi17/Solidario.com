from django import forms
from .models import Doacao,DoacaoRec,Doadores
class DoacaoForm(forms.ModelForm):

    class Meta:
        model = Doacao
        exclude = ['status_doacao','data_abertura','recebedor']
        labels = {
            'urgencia': 'Nível de Urgência',
            'modo_entrega': 'Modo de Entrega',
            'doacao_item': 'Item da Doação',
            'quantidade':'Quantidade'

        }
        widgets = {
            'urgencia': forms.Select(attrs={'class': 'form-control'}),
            'modo_entrega': forms.Select(attrs={'class': 'form-control'}),
            'doacao_item': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DoacaoRecForm(forms.ModelForm):
    class Meta:
        model = DoacaoRec
        fields = ['data_combinada', 'doador', 'doacao_pedido', 'quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doacao_pedido'].queryset = Doacao.objects.all()
        self.fields['doador'].queryset = Doadores.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        quantidade = cleaned_data.get("quantidade")
        doacao_pedido = cleaned_data.get("doacao_pedido")

        if doacao_pedido and quantidade > doacao_pedido.quantidade:
            raise forms.ValidationError("A quantidade recebida não pode ser maior que a quantidade da doação.")

        return cleaned_data
