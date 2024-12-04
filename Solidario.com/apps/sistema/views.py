from django.shortcuts import render,redirect
from .forms import LoginForm,CadastroForm,CadastroRecebedorForm
from django.contrib.auth.models import User
from django.contrib import auth,messages
from apps.doador.models import Doadores
from apps.recebedores.models import Recebedores
from validate_docbr import CPF,CNPJ
from .api import con_cep_status,con_cep_encontrado
import re
def index(request):
    """Pagina inicial do sistema"""
    return render(request,'index.html')

def login(request):
    """View de login, onde os usuarios utilizam seu nickname e senha para entrarem ao sistema.
    Nessa view os usuarios são redirecionados para as rotas de seus tipos de perfis.
    Assim, doadores e recebedores não tem acesso a rotas não destinadas a eles"""

    #Puxar o formulário de login
    form = LoginForm()

    #Receber informações do usuario
    if request.method == 'POST':
        form = LoginForm(request.POST)

        #Validar formulário
        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()

            #Autenticar usuario
            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            #Validar entrada do usuario no sistema
            if usuario != None:
                auth.login(request,usuario)

                #Direcionar o usuario para telas de doadores
                if Doadores.objects.filter(usuario = usuario).exists():
                    return redirect('doador_inicio')
                #Direcionar o usuario para telas de doadores
                else:
                    return redirect('recebedor_inicio')
            #Retornar mensagem de erro para usuario e senha
            else:
                messages.error(request,"Usuario ou senha incorretos")
                return redirect('login')

    return render(request,'login.html',{"form":form})

def cadastro(request):
    """Essa view é destinada para cadastrar doadores no sistema
       Receber os dados do doador, valida-los e adiciona-lo no sistema"""
    #puxar o formulario
    form = CadastroForm()


    if request.method == "POST":
        form = CadastroForm(request.POST)

        #Validar formulario e seus campos
        if form.is_valid():
            nome = form["nome_cad"].value()
            email = form["email_cad"].value()
            senha1 = form["senha_cad"].value()
            senha2 = form["senha_cad2"].value()
            cpf = form["cpf_cad"].value()
            cep = form["cep_cad"].value()
            telefone = form["telefone_cad"].value()

            #Validar CPF
            cpf_val = CPF()
            if not cpf_val.validate(cpf):
                messages.error(request, "CPF inválido, use só numeros")
                return redirect('cadastro')

            #Validar cep
            if con_cep_status(cep) == 400:
                messages.error(request,"CEP invalido")
                return redirect('cadastro')

            #Validar telefone
            if not re.fullmatch(r"^\d{11}$", telefone):
                messages.error(request, "Número de telefone inválido, use somente números")
                return redirect('cadastro')

            # Validar coincidencia das senhas
            if senha1 != senha2:
                messages.error(request, "Senhas não coincidem")
                return redirect('cadastro')

            #Validar se já existe usuario com esse nome
            if User.objects.filter(username = nome).exists():
                messages.error(request, "Usuario já existente")
                return redirect('cadastro')

            #Adicionar usuario a tabela usuarios e doador
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha2
            )
            usuario.save()

            doador = Doadores.objects.create(
                usuario = usuario,
                nm_doador = nome,
                cpf = cpf,
                cep = cep,
                telefone = telefone,
                historico_doacoes = 0

            )
            doador.save()

            return redirect('login')
        #Mensagem de erro caso algo esteja invalido
        else:
            messages.error(request, "CPF,CEP ou TELEFONE inválidos, revise as respostas")
            return redirect('cadastro')

    return render(request,'cadastro.html',{"form":form})

def cadastro_recebedor(request):
    form = CadastroRecebedorForm()

    if request.method == "POST":
        form = CadastroRecebedorForm(request.POST)

        if form.is_valid():
            nome = form["nome_cad"].value()
            email = form["email_cad"].value()
            senha1 = form["senha_cad"].value()
            senha2 = form["senha_cad2"].value()
            cnpj = form["cnpj_cad"].value()
            cep = form["cep_cad"].value()
            telefone = form["telefone_cad"].value()
            pix = form["pix_cad"].value()

            cnpj_val = CNPJ()
            if not cnpj_val.validate(cnpj):
                messages.error(request, "CNPJ inválido")
                return redirect('cadastro')

            if con_cep_status(cep) == 400:
                messages.error(request,"CEP invalido, use só numeros")
                return redirect('cadastro')

            resultado = con_cep_encontrado(cep)
            if resultado.get("erro") == "true":
                messages.error(request, "CEP não encontrado")
                return redirect('cadastro')

            if not re.fullmatch(r"^\d{11}$", telefone):
                messages.error(request, "Formato: 71999998888")
                return redirect('cadastro')

            if senha1 != senha2:
                messages.error(request, "Senhas não coincidem")
                return redirect('cadastro_recebedor')

            if User.objects.filter(username = nome).exists():
                messages.error(request, "Usuario já existente")
                return redirect('cadastro_recebedor')

            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha2
            )

            usuario.save()

            recebedor = Recebedores.objects.create(
                usuario = usuario,
                nm_recebedor = nome,
                cnpj = cnpj,
                cep = cep,
                pix = pix,
                telefone = telefone


            )
            recebedor.save()

            return redirect('login')
        else:
            messages.error(request, "CPF,CEP ou TELEFONE inválidos, revise as respostas")
            return redirect('cadastro')


    return render(request,'cadastro_recebedor.html',{"form":form})

def logout(request):
    """Usuario desconectar do sistema"""
    auth.logout(request)
    messages.success(request,"Logout feito")
    return redirect('login')
    #valiadr alguma coisa
