# pwsite/urls.py
from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'cursosV2'

urlpatterns = [
    path('cursoV2/', views.inicio_view, name='cursos'),
    path('cursoV2/<int:id_curso>', views.curso_view, name='curso'),
    path('cursoV2/<str:nome>', views.disciplina_view, name='disciplina'),
    path('projeto/<int:id_projeto>/', views.projeto_view, name='projeto'),
    path('registo/', views.registo_view, name="registo"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]