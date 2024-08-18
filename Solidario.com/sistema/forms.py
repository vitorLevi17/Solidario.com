from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex.Doador Oliveira"
            }
        )
    )
    senha_login = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Insira a Senha"
            }
        )
    )
class CadastroForm(forms.Form):
    nome_cad = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex.Doador Oliveira"
            }
        )
    )
    senha_cad = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Insira a Senha"
            }
        )
    )
    senha_cad2 = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme a senha"
            }
        )
    )




