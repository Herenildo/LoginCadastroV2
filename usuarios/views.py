from ast import Try
from asyncio import constants
import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import redirect
from hashlib import sha256
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def login (request):
    messages.add_message(request,  constants.SUCCESS, 'Você foi logado com sucesso,Seja bem vindo!')
    status = request.GET.get('status')
    return render(request, 'login.html',{'status':status})

def cadastro (request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status})

def valida_cadastro (request):
    nome = request.POST.get('nome', '').strip()
    email = request.POST.get('email','').strip()
    senha = request.POST.get('senha','').strip()

    if not nome or not email:
        messages.add_message(request, constants.ERROR, 'Nome ou email vazio!')
        return redirect('/auth/cadastro/')

    if not senha or len(senha) < 8:
        messages.add_message(request, constants.ERROR, 'Senha nao pode ter menos de 8 caracteres!')
        return redirect('/auth/cadastro/')
    


    usuario = Usuarios.objects.filter(email=email)

    if len(usuario) > 0:
        messages.add_message(request, constants.ERROR, 'Email ja cadastrado!')
        return redirect('/auth/cadastro/')
    
    try:
        senha = sha256(senha.encode()).hexdigest()    

        usuario = Usuarios(nome=nome, 
                        email=email, 
                        senha=senha)

        usuario.save()
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
        return redirect('/auth/cadastro/')
    
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema!')
        return redirect('/auth/cadastro/')

def valida_login (request):
    email = request.POST.get('email','').strip()
    senha = request.POST.get('senha','').strip()
    
    
    senha = sha256(senha.encode()).hexdigest() 
    
    usuario = Usuarios.objects.filter(email=email).filter(senha=senha)
    

    if len(usuario) == 0:
        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
    elif len(usuario) > 0:
        request.session['logado'] = True
        request.session['usuario'] = usuario[0].id
        return redirect('/plataforma/home/')
        
 

def sair(request):
    request.session.flush()
    messages.add_message(request, constants.WARNING, 'Faá login antes de acessar a plataformar!')
    return redirect('/auth/login/')


#    try:
#        del request.session['logado']
#        return redirect('/auth/login/')
#    except KeyError:
#        return redirect('auth/login/?status=3')


    
