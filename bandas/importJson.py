from bandas.models import Banda
from bandas.models import Musica
from bandas.models import Album
import json

with open('bandas/bandas.json') as f:
    bandas = json.load(f)


    for name, info in bandas.items():
        Banda.objects.create(
            nome = name,
            nacionalidade = info['nacionalidade'],
            anoCriacao = info['anoCriacao']
        )

with open('bandas/albuns.json') as f:
    albuns = json.load(f)

    for info_album in albuns:
    # Criar o álbum
        album = Album.objects.create(
        nome=info_album['nome_album'],
        ano_lancamento=info_album['ano_lancamento_album'],
        banda=Banda.objects.get(nome=info_album['banda_album']),
        capa=info_album['capa_album'],
        )
        for info_musica in info_album['musicas']:
        # Criar uma nova música e associá-la ao álbum
            Musica.objects.create(
            nome=info_musica['nome_musica'],
            ano_lancamento=info_musica['ano_lancamento_musica'],
            link=info_musica['link_musica'],
            duracao=info_musica['duracao_musica'],
            banda = Banda.objects.get(nome=info_album['banda_album']),
            )



