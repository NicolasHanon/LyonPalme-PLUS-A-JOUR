from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from planning.models import *

# Create your views here.
def indexMain(request):
    """
    Affiche la page d'accueil du site web pour l'application PalmPlanning

    **Template:**

    :template:`main/index.html`
    """
    return render(request, "main/index.html")

@login_required(login_url='login_user')
def indexApp(request):
    """
    Affiche la page d'accueil de l'application planning

    **Context:**

    `usr`
        Une instance du modèle :model:`planning.ENTRAINEUR`

    **Template:**

    :template:`planning/index.html`
    """
    usr = ENTRAINEUR.objects.get(UserId=request.user)
    return render(request, "planning/index.html", {'usr': usr})

def login_user(request):
    """
    Affiche la page de connexion de l'application planning

    **Template:**

    :template:`planning/login.html`
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('indexApp')
        else:
            error = "Mauvais identifiants de connexion"
            return render(request, 'planning/login.html', {'error': error})
    return render(request, 'planning/login.html')

@login_required(login_url='login_user')
def logout_user(request):
    """
    Vue de déconnexion de l'application planning
    """
    logout(request)
    return redirect('indexMain')