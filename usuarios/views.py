from ast import Try
import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuarios
from django.shortcuts import redirect
from hashlib import sha256

# Create your views here.
def login (request):
    status = request.GET.get('status')
    return render(request, 'login.html',{'status':status})

def cadastro (request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status})

def valida_cadastro (request):
    nome = request.POST.get('nome', '').strip()
    email = request.POST.get('email','').strip()
    senha = request.POST.get('senha','').strip()

    if not senha or len(senha) < 8:
        return redirect('/auth/cadastro/?status=2')
    
    if not senha or len(senha) < 8:
        redirect('/auth/cadastro/?status=2')

    usuario = Usuarios.objects.filter(email=email)

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=3')
    
    try:
        senha = sha256(senha.encode()).hexdigest()    

        usuario = Usuarios(nome=nome, 
                        email=email, 
                        senha=senha)

        usuario.save()
    
        return redirect('/auth/cadastro/?status=0')
    
    except:
    
        return redirect('/auth/cadastro/?status=4')

def valida_login (request):
    email = request.POST.get('email','').strip()
    senha = request.POST.get('senha','').strip()
    
    
    senha = sha256(senha.encode()).hexdigest() 
    
    usuario = Usuarios.objects.filter(email=email).filter(senha=senha)
    

    if len(usuario) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuario) > 0:
        request.session['logado'] = True
        request.session['usuario'] = usuario[0].id
        return redirect('/plataforma/home/')
        
        
        




def sair(request):
    try:
        del request.session['logado']
        return redirect('/auth/login/')
    except KeyError:
        return redirect('auth/login/?status=3')


    
