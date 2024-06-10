from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .models import *
from .forms import *

# Create your views here.
def pagina_view(request):


    return render(request, "Uni/index.html")

def curso_view(request):
    anos = range(1, 4)
    context = {
      'cursos': Curso1.objects.all(),
      'anos': anos
    }

    return render(request, "Uni/curso.html", context)

def cadeira_view(request, cadeira_id):
    context ={
        'cadeira' : Cadeira1.objects.get(id = cadeira_id),
    }
    return render(request, "Uni/cadeira.html", context)

def cadeiras_view(request, ano):
    cadeiras = Cadeira1.objects.filter(ano=ano)
    context = {
        'cadeiras': cadeiras,
        'ano': ano,
    }
    return render(request, "Uni/cadeiras.html", context)

def projetos_view(request):
    context ={
        'projetos' : Projeto1.objects.all(),
    }
    return render(request, "Uni/projetos.html", context)

def projeto_view(request, projeto_id):
    context ={
        'projeto' : Projeto1.objects.get(id = projeto_id),
    }
    return render(request, "Uni/projeto.html", context)



