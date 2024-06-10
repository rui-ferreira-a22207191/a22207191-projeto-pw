from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'meteo'

urlpatterns = [
  path('inicio/', views.inicio_view, name='Meteorologia'),
  path('cidades/', views.cidades_view, name='MeteorologiaCidades'),
  path('cidade/<int:globalIdLocal>/', views.get_cityDetails_view, name='DetalhesCidade'),
  path('api/', views.api_view, name='API'),
  path('cidadeAPI/', views.api_cidades, name='get_cidades'),
  path('weathertype/', views.api_weather_type, name='get_weather_type'),
  path('cidadeAPI/<int:globalIdLocal>/', views.api_temposemana, name='get_temposemana'),
  path('cidadeTodayAPI/<int:globalIdLocal>/', views.api_today_forecast, name='get_tempohoje'),
]
