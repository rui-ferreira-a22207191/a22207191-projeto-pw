# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'bandas'

urlpatterns = [
    path('inicio/', views.pagina_view, name='PaginaInicial'),
    path('bandas/', views.inicio_view, name='bandas'),
    path('albuns/', views.albuns_view, name='albuns'),
    path('musicas/', views.musicas_view, name='musicas'),
    path('bandaInfo/<int:banda_id>', views.banda_view, name='bandaInfo'),
    path('musicaInfo/<int:musica_id>', views.musica_view, name='musicaInfo'),
    path('albunsInfo/<int:album_id>', views.albunsInfo_view, name='albunsInfo'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('bandaInfo/novo', views.novo_banda_view, name="novo_banda"),
    path('bandaInfo/<int:banda_id>/edita', views.edita_banda_view,name="edita_banda"),
    path('bandaInfo/<int:banda_id>/apaga', views.apaga_banda_view,name="apaga_banda"),
    path('userBandas/', views.user_view, name='User'),
    path('musicaInfo/novo', views.novo_musica_view, name="novo_musica"),
    path('musicaInfo/<int:musica_id>/edita', views.edita_musica_view,name="edita_musica"),
    path('musicaInfo/<int:musica_id>/apaga', views.apaga_musica_view,name="apaga_musica"),
    path('albumInfo/novo', views.novo_album_view, name="novo_album"),
    path('albumInfo/<int:album_id>/edita', views.edita_album_view,name="edita_album"),
    path('albumInfo/<int:album_id>/apaga', views.apaga_album_view,name="apaga_album"),
]