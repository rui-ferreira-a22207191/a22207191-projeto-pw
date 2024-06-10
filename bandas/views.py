from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, models
from .models import *
from .forms import *

def pagina_view(request):

    return render(request, "bandas/paginaInicial.html")

def user_view(request):

    return render(request, "bandas/user.html")

def inicio_view(request):
    context = {
      'bandas': Banda.objects.all(),
   }
    return render(request, "bandas/inicio.html", context)

def banda_view(request, banda_id):
    context = {
        'banda' : Banda.objects.get(id = banda_id),
   }
    return render(request, "bandas/bandas.html", context)

def musica_view(request, musica_id):
    context = {
        'musica' : Musica.objects.get(id = musica_id),
   }
    return render(request, "bandas/musica.html", context)

def albuns_view(request):
    context = {
      'albuns': Album.objects.all(),
   }
    return render(request, "bandas/albuns.html", context)

def albunsInfo_view(request, album_id):
    context = {
        'album' : Album.objects.get(id = album_id),
   }
    return render(request, "bandas/albunsInfo.html", context)

def musicas_view(request):
    context = {
      'musicas': Musica.objects.all(),
   }
    return render(request, "bandas/musicasList.html", context)


def registo_view(request):
    if request.method == "POST":
        models.User.objects.create_user(
            username=request.POST['username'],
            email=request.POST['email'],
            first_name=request.POST['nome'],
            last_name=request.POST['apelido'],
            password=request.POST['password']
        )
        return redirect('bandas:login')

    return render(request, 'bandas/registo.html')

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('bandas:User')
        else:
            render(request, 'bandas/login.html', {
                'mensagem':'Credenciais inválidas'
            })

    return render(request, 'bandas/login.html')

def logout_view(request):
    logout(request)
    return redirect('bandas:login')

def novo_banda_view(request):

    form = BandaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:bandas')

    context = {'form': form}
    return render(request, 'bandas/novo_banda.html', context)


def edita_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)

    if request.POST:
        form = BandaForm(request.POST or None, request.FILES, instance=banda)
        if form.is_valid():
            form.save()
            return redirect('bandas:bandaInfo')
    else:
        form = BandaForm(instance=banda)  # cria formulário com dados da instância autor

    context = {'form': form, 'banda':banda}
    return render(request, 'bandas/edita_banda.html', context)

def apaga_banda_view(request, banda_id):
    banda = Banda.objects.get(id=banda_id)
    banda.delete()
    return redirect('bandas:bandas')

def novo_musica_view(request):

    form = MusicaForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:musicas')

    context = {'form': form}
    return render(request, 'bandas/novo_musica.html', context)

def novo_album_view(request):

    form = AlbumForm(request.POST or None, request.FILES)  # request.FILES deve ser incluido se forem enviados ficheiros ou imagens
    if form.is_valid():
        form.save()
        return redirect('bandas:albuns')

    context = {'form': form}
    return render(request, 'bandas/novo_album.html', context)

def edita_album_view(request, album_id):
    album = Album.objects.get(id=album_id)

    if request.POST:
        form = AlbumForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:albumInfo')
    else:
        form = AlbumForm(instance=album)  # cria formulário com dados da instância autor

    context = {'form': form, 'album':album}
    return render(request, 'bandas/edita_album.html', context)

def apaga_album_view(request, album_id):
    album = Album.objects.get(id=album_id)
    album.delete()
    return redirect('bandas:albuns')

def edita_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)

    if request.POST:
        form = MusicaForm(request.POST or None, request.FILES, instance=musica)
        if form.is_valid():
            form.save()
            return redirect('bandas:musicaInfo')
    else:
        form = MusicaForm(instance=musica)  # cria formulário com dados da instância autor

    context = {'form': form, 'musica':musica}
    return render(request, 'bandas/edita_musica.html', context)

def apaga_musica_view(request, musica_id):
    musica = Musica.objects.get(id=musica_id)
    musica.delete()
    return redirect('bandas:musicas')