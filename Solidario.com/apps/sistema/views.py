from django.shortcuts import render,redirect
from .forms import LoginForm,CadastroForm
from django.contrib.auth.models import User
from django.contrib import auth,messages
from apps.doador.models import Doadores

def index(request):
    return render(request,'index.html')

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)


        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()


            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            if usuario != None:
                auth.login(request,usuario)
                if Doadores.objects.filter(usuario = usuario).exists():
                    return redirect('doador_inicio')
                else:
                    return redirect('recebedor_inicio')
            else:
                messages.error(request,"Usuario ou senha incorretos")
                return redirect('login')


    return render(request,'login.html',{"form":form})

def cadastro(request):
    form = CadastroForm()

    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            nome = form["nome_cad"].value()
            email = form["email_cad"].value()
            senha1 = form["senha_cad"].value()
            senha2 = form["senha_cad2"].value()
            cpf = form["cpf_cad"].value()
            cep = form["cep_cad"].value()
            telefone = form["telefone_cad"].value()

            if senha1 != senha2:
                messages.error(request, "Senhas não coincidem")
                return redirect('cadastro')

            if User.objects.filter(username = nome).exists():
                messages.error(request, "Usuario já existente")
                return redirect('cadastro')

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

            return redirect('index')

    return render(request,'cadastro.html',{"form":form})

def logout(request):
    auth.logout(request)
    messages.success(request,"Logout feito")
    return redirect('login')

