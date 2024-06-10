# pwsite/urls.py
from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandasrap'

urlpatterns = [
    path('inicio/', views.pagina_view, name='inicio'),
    path('artistas/', views.artistas_view, name='artistas'),
    path('artista/<int:artista_id>', views.artista_view, name='artista'),
    path('albuns/', views.albuns_view, name='albuns'),
    path('album/<int:album_id>', views.album_view, name='album'),
    path('musicas/', views.musicas_view, name='musicas'),
    path('musica/<int:musica_id>', views.musica_view, name='musica'),
    path('login/', views.login_view, name="login"),
    path('registo/', views.registo_view, name="registo"),
    path('logout/', views.logout_view, name="logout"),
    path('user/', views.user_view, name="user"),
    path('artista/novo', views.novo_artista_view, name="novo_artista"),
    path('album/novo', views.novo_album_view, name="novo_album"),
    path('musica/nova', views.nova_musica_view, name="nova_musica"),
    path('artista/<int:artista_id>/apaga', views.apaga_artista_view,name="apaga_artista"),
    path('album/<int:album_id>/apaga', views.apaga_album_view,name="apaga_album"),
    path('musica/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),
    path('album/<int:album_id>/edita', views.edita_album_view,name="edita_album"),
    path('artista/<int:artista_id>/edita', views.edita_artista_view,name="edita_artista"),
    path('musica/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),
]
