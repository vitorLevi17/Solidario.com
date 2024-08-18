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




