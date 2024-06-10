from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .models import *

# Create your views here.
def inicio_view(request):
    context = {
      'cursos': Curso.objects.all(),
   }
    return render(request, "cursoV2/cursos.html", context)

def curso_view(request,id_curso):
    context = {
      'curso': Curso.objects.get(id = id_curso),
   }
    return render(request, "cursoV2/curso.html", context)

def disciplina_view(request, nome):
    disciplina = Disciplina.objects.get(nome=nome)
    context = {'disciplina': disciplina}
    return render(request, "cursoV2/disciplina.html", context)

def projeto_view(request, id_projeto):
    projeto = Projeto.objects.get(id=id_projeto)
    context = {'projeto': projeto}
    return render(request, "cursoV2/projeto.html", context)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('cursosV2:login')

    return render(request, 'cursoV2/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('cursosV2:cursos')
        else:
            render(request, 'cursoV2/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'cursoV2/login.html')

def logout_view(request):
    logout(request)
    return redirect('cursosV2:login')