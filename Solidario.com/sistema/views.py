from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import auth,messages

def index(request):
    return render(request,'index.html')

def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("1 cond")

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha_login"].value()


            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            print("2 cond")
            if usuario != None:
                auth.login(request,usuario)
                return redirect('index')
            else:
                messages.error(request,"Usuario ou senha incorretos")
                return redirect('login')


    return render(request,'login.html',{"form":form})

def cadastro(request):
    return render(request,'cadastro.html')
