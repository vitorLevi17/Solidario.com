from django.shortcuts import render,redirect
from .forms import LoginForm,CadForm
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request,'index.html')

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            if usuario != None:
                auth.login(request,usuario)
                return redirect('doador_index')
            else:
                error_message = "Usuário ou senha incorretos."

    return render(request,'login.html',{"form":form})

def cadastro(request):
    form = CadForm()

    if request.method == 'POST':
        form = CadForm(request.POST)

        if form.is_valid():

            nome = form["username"].value()
            senha = form["password"].value()
            senha1 = form["password1"].value()

            if senha != senha1:
                error_message = "As senhas não coincidem."
                return render(request, 'cadastro.html', {"form": form})

            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                password=senha

            )
            usuario.save()
            return redirect('login')

    return render(request,'cadastro.html')

def doador_index(request):
    return render(request,'doador_index.html')

