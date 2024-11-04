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
                "placeholder": "Ex. Doador Oliveira"
            }
        )
    )
    email_cad = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ex.DoadorOliveira@gmail.com"
            }
        )
    )
    cpf_cad = forms.CharField(
        label="CPF",
        required=True,
        max_length=11,  # CPF tem no máximo 11 caracteres
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Somente números"
            }
        )
    )
    cep_cad = forms.CharField(
        label="CEP",
        required=True,
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Somente números"
            }
        )
    )
    complemento_cad = forms.CharField(
        label="Complemento",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Próximo a loja X"
            }
        )

    )
    telefone_cad = forms.CharField(
        label="Telefone",
        required=True,
        max_length=13,
        widget=forms.TextInput(
            attrs={
                "placeholder": "71999998888"
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
        label="Confirme a Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme a senha"
            }
        )
    )
class CadastroRecebedorForm(forms.Form):
    nome_cad = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex. Doador Oliveira"
            }
        )
    )
    email_cad = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Ex.DoadorOliveira@gmail.com"
            }
        )
    )
    cnpj_cad = forms.CharField(
        label="cnpj",
        required=True,
        max_length=14,
        widget=forms.TextInput(
            attrs = {
                "placeholder": "Somente números"
            }
        )
    )
    cep_cad = forms.CharField(
        label="CEP",
        required=True,
        max_length=8,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Somente números"
            }
        )
    )

    telefone_cad = forms.CharField(
        label="Telefone",
        required=True,
        max_length=13,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Somente números"
            }
        )
    )
    pix_cad = forms.CharField(
        label="Pix",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Insira sua chave pix"
            }
        )
    )
    complemento_cad = forms.CharField(
        label="Complemento",
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Próximo a loja X"
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
        label="Confirme a Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirme a senha"
            }
        )
    )