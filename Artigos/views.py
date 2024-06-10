from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .models import *
from .forms import *

# Create your views here.
def index_view(request):
    context = {
      'artigos': Artigo.objects.all(),
   }
    return render(request, "Artigos/index.html", context)
def user_view(request):

    return render(request, "Artigos/user.html")

def artigo_view(request, artigo_id):
    context = {
        'artigo' : Artigo.objects.get(id = artigo_id),
   }
    return render(request, "Artigos/Artigo.html", context)

def autor_view(request, autor_id):
    context = {
        'autor' : Autor.objects.get(id = autor_id),
   }
    return render(request, "Artigos/Autor.html", context)

def listaGenero_view(request, genero):
    # Filtrar os artigos pelo gênero fornecido
    artigos = Artigo.objects.filter(genero=genero)
    context = {
        'artigos': artigos,
        'genero': genero,
    }
    return render(request, 'Artigos/artigosgenero.html', context)

def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('Artigos:login')

    return render(request, 'Artigos/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('Artigos:User')
        else:
            render(request, 'Artigos/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'Artigos/login.html')

def logout_view(request):
    logout(request)
    return redirect('Artigos:login')



def novo_artigo_view(request):

    form = ArtigoForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('Artigos:Artigos')

    context = {'form': form}
    return render(request, 'Artigos/novo_Artigo.html', context)


def edita_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)

    if request.POST:
        form = ArtigoForm(request.POST or None, request.FILES, instance=artigo)
        if form.is_valid():
            form.save()
            return redirect('Artigos:Artigos')
    else:
        form = ArtigoForm(instance=artigo)  # cria formulário com dados da instância autor

    context = {'form': form, 'artigo':artigo}
    return render(request, 'Artigos/edita_artigo.html', context)

def apaga_artigo_view(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    artigo.delete()
    return redirect('Artigos:Artigos')

def novo_autor_view(request):

    form = AutorForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('Artigos:Artigos')

    context = {'form': form}
    return render(request, 'Artigos/novo_Autor.html', context)

def novo_comentario_view(request):

    form = ComentarioForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('Artigos:Artigo')

    context = {'form': form}
    return render(request, 'Artigos/novo_comentario.html', context)

