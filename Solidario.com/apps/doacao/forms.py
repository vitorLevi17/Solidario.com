from django import forms
from .models import Doacao
class DoacaoForm(forms.ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'
        labels = {
            'urgencia': 'Nível de Urgência',
            'modo_entrega': 'Modo de Entrega',
            'status_doacao': 'Status da Doação',
            'recebedor': 'Recebedor',
            'doacao_item': 'Item da Doação'
        }
        widgets = {
            'urgencia': forms.Select(attrs={'class': 'form-control'}),
            'modo_entrega': forms.Select(attrs={'class': 'form-control'}),
            'status_doacao': forms.Select(attrs={'class': 'form-control'}),
            'data_abertura': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'recebedor': forms.Select(attrs={'class': 'form-control'}),
            'doacao_item': forms.Select(attrs={'class': 'form-control'}),
        }
