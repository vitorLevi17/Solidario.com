from django import forms
from .models import Doacao,DoacaoRec
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
        fields = ['data_combinada', 'quantidade']
        labels = {
            'data_combinada':'Data de doação',
            'quantidade':'Quantidade',
        }
        widgets = {
            'data_combinada': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'})
        }
