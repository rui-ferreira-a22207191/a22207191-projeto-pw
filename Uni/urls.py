from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'Uni'

urlpatterns = [
    path('inicio/', views.pagina_view, name='inicio'),
    path('curso/', views.curso_view, name='curso'),
    path('cadeira/<int:cadeira_id>', views.cadeira_view, name='cadeira'),
    path('cadeiras/<int:ano>', views.cadeiras_view, name='cadeiras'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('projeto/<int:projeto_id>', views.projeto_view, name='projeto'),
]