# Artigos/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'Artigos'

urlpatterns = [
  path('Artigos/', views.index_view, name='Artigos'),
  path('ArtigosUser/', views.user_view, name='User'),
  path('Artigo/<int:artigo_id>', views.artigo_view, name='artigo'),
  path('Autor/<int:autor_id>', views.autor_view, name='autor'),
  path('Artigos/<str:genero>', views.listaGenero_view, name='artigosGenero'),
  path('registo/', views.registo_view, name="registo"),
  path('login/', views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout"),
  path('Artigo/novo', views.novo_artigo_view, name="novo_artigo"),
  path('Artigo/<int:artigo_id>/edita', views.edita_artigo_view,name="edita_artigo"),
  path('Artigo/<int:artigo_id>/apaga', views.apaga_artigo_view,name="apaga_artigo"),
  path('Autor/novo', views.novo_autor_view, name="novo_autor"),
  path('Comentario/novo', views.novo_comentario_view, name="novo_comentario"),


]
