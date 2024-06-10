from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('BytedeSabor/', views.inicio_view, name='BytedeSabor'),
    path('SobreMim/', views.sobre_view, name='SobreMim'),
    path('bolodechocolate/', views.bolo_view, name='BoloDeChocolate'),
    path('receitas/', views.receitas_view, name='Receitas'),
]