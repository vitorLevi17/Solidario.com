from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário',max_length=255)
    password = forms.CharField(label='Senha',widget=forms.PasswordInput())

class CadForm(forms.Form):
    username = forms.CharField(label='Usuário', max_length=255)
    password = forms.CharField(label='Senha', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput())



