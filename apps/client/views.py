from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Info

def getInfos():
    info = Info.objects.get(admin='luhdev')

    if info == None:
        url_youtube = ''
        url_instagram = ''
        url_github = ''
        url_group_whatsapp = ''
    else: 
        url_youtube = info.url_youtube_admin
        url_instagram = info.url_instagram_admin
        url_github = info.url_github_admin
        url_group_whatsapp = info.url_group_whatsapp

    return {"url_youtube": url_youtube, "url_instagram": url_instagram, "url_github": url_github, "url_group_whatsapp": url_group_whatsapp}

# Create your views here.
def index(request):
    if not request.user.is_authenticated:

        infos = getInfos()

        return render(request, 'pages/landing-page.html', infos)
    else:
        return redirect('homepage')


def fazer_login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    
    infos = getInfos()

    if(request.method == 'POST'):

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            # Se as credenciais forem inválidas, exibir uma mensagem de erro
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('login')
    else:
        return render(request, 'pages/login.html', infos)
    

def homepage(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    return render(request, 'pages/homepage.html')

def fazer_logout(request):
    if not request.user.is_authenticated:
        return redirect('index')
    
    logout(request)
    return redirect('index')