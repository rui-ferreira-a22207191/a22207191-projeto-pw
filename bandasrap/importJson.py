import json
from .models import Artista

with open('bandasrap/artista.json') as f:
    data = json.load(f)
    for item in data:
        Artista.objects.create(
            nome=item['nome'],
            nacionalidade=item['nacionalidade'],
            ano_criacao=item['ano_criacao'],
            biografia=item['biografia'],
        )
