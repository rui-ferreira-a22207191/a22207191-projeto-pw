from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import requests

def get_data_citys():
    url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(url)

    if response.status_code == 200:
        dic_dados = response.json()
        context = {
            'data': dic_dados['data']
        }
        return context
    else:
        return {'data': []}

def get_dic_weather():
    url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    response = requests.get(url)

    if response.status_code == 200:
        weather_types = response.json()['data']
        weather_dict = {wt['idWeatherType']: wt['descWeatherTypePT'] for wt in weather_types}
        return weather_dict
    return {}

def get_weekly_forecast(globalIdLocal):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json'
    response = requests.get(url)

    if response.status_code == 200:
        forecast_data = response.json()
        weather_dict = get_dic_weather()

        for forecast in forecast_data['data']:
            # Adicionar a descrição do tempo
            forecast['weather_description'] = weather_dict.get(forecast['idWeatherType'], 'Não tem descrição')

        return forecast_data
    else:
        return {'data': []}


def get_today_forecast(globalIdLocal):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json'
    response = requests.get(url)

    if response.status_code == 200:
        forecast_data = response.json()
        weather_dict = get_dic_weather()

        if forecast_data['data']:
            today_forecast = forecast_data['data'][0]
            today_forecast['weather_description'] = weather_dict.get(today_forecast['idWeatherType'], 'Não tem descrição')
            return today_forecast
        else:
            return {'error': 'No forecast data available'}
    else:
        return {'error': 'Could not retrieve data'}


def get_cityDetails_view(request, globalIdLocal):
    url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{globalIdLocal}.json'
    response = requests.get(url)

    if response.status_code == 200:
        cidade_detalhes = response.json()
        weather_dict = get_dic_weather()

        for forecast in cidade_detalhes['data']:
            # Adicionar a descrição do tempo
            forecast['weather_description'] = weather_dict.get(forecast['idWeatherType'], 'Não tem descrição')

        # Adicionar o nome da cidade
        cidades = get_data_citys()['data']
        cidade_nome = next((cidade['local'] for cidade in cidades if cidade['globalIdLocal'] == globalIdLocal), 'Local desconhecido')

        context = {
            'cidade_detalhes': cidade_detalhes,
            'cidade_nome': cidade_nome
        }

        return render(request, "meteo/cidade_detalhes.html", context)

def inicio_view(request):
    context = get_data_citys()
    return render(request, "meteo/inicio.html", context)

def cidades_view(request):
    context = get_data_citys()
    return render(request, "meteo/cidades_lista.html", context)


def api_view(request):

    return render(request, "meteo/API.html")


def api_cidades(request):

    content = get_data_citys()
    return JsonResponse(content)


def api_temposemana(request, globalIdLocal):

    content = get_weekly_forecast(globalIdLocal)
    return JsonResponse(content)

def api_weather_type(request):

    content = get_dic_weather()
    return JsonResponse(content)

def api_today_forecast(request, globalIdLocal):
    content = get_today_forecast(globalIdLocal)
    return JsonResponse(content)














