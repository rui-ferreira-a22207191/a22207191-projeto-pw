from django.shortcuts import render, redirect
from django.contrib.auth import models
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.
def pagina_view(request):

    return render(request, "bandasrap/index.html")

def artistas_view(request):
    context = {
      'artistas': Artista.objects.all(),
   }
    return render(request, "bandasrap/artistaslist.html", context)

def artista_view(request, artista_id):
    context = {
        'artista' : Artista.objects.get(id = artista_id),
   }
    return render(request, "bandasrap/artista.html", context)

def albuns_view(request):
    context = {
      'albuns': Album.objects.all(),
   }
    return render(request, "bandasrap/albunslist.html", context)

def album_view(request, album_id):
    context = {
        'album' : Album.objects.get(id = album_id),
   }
    return render(request, "bandasrap/album.html", context)

def musicas_view(request):
    context = {
      'musicas': Musica.objects.all(),
   }
    return render(request, "bandasrap/musicaslist.html", context)

def musica_view(request, musica_id):
    context = {
        'musica' : Musica.objects.get(id = musica_id),
   }
    return render(request, "bandasrap/musica.html", context)

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return render(request, 'bandasrap/user.html')
        else:
            render(request, 'bandasrap/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandasrap/login.html')

def registo_view(request):
    if request.method == "POST":
        User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandasrap:login')

    return render(request, 'bandasrap/registo.html')

def logout_view(request):

    logout(request)
    return redirect('bandasrap:login')

def user_view(request):

    return render(request, "bandasrap/user.html")


def novo_artista_view(request):

    form = ArtistaForm()      # form é uma instancia de AutorForm,
                            # formulário em branco com os campos de Autor

    context = {'form': form}
    return render(request, 'bandasrap/novo_artista.html', context)

def novo_album_view(request):

    form = AlbumForm()      # form é uma instancia de AutorForm,
                            # formulário em branco com os campos de Autor

    context = {'form': form}
    return render(request, 'bandasrap/novo_album.html', context)

def nova_musica_view(request):

    form = MusicaForm()      # form é uma instancia de AutorForm,
                            # formulário em branco com os campos de Autor

    context = {'form': form}
    return render(request, 'bandasrap/nova_musica.html', context)

def apaga_artista_view(request, artista_id):
    artista = Artista.objects.get(id=artista_id)
    artista.delete()
    return redirect('bandasrap:artistas')

def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandasrap:albuns')

def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandasrap:musicas')


def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandasrap:albuns')
    else:
        form = AlbumForm(instance=album)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album}
    return render(request, 'bandasrap/edita_album.html', context)


def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandasrap:musicas')
    else:
        form = MusicaForm(instance=musica)  # cria formulário com dados da instância autor

    context = {'form': form, 'musica':musica}
    return render(request, 'bandasrap/edita_musica.html', context)

def edita_artista_view(request, artista_id):
    artista = Artista.objects.get(id=artista_id)

    if request.POST:
        form = ArtistaForm(request.POST or None, request.FILES, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('bandasrap:artistas')
    else:
        form = ArtistaForm(instance=artista)  # cria formulário com dados da instância autor

    context = {'form': form, 'artista':artista}
    return render(request, 'bandasrap/edita_artista.html', context)





