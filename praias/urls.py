from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'praias'

urlpatterns = [
  path('praias/', views.index_view, name='praias'),
  path('praia/<int:id_praia>', views.praia_view, name='praia'),
]