from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200, null=True, blank=True)
    ano_criacao = models.IntegerField()
    foto = models.ImageField(null=True, blank=True)
    biografia = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField()
    link = models.URLField(max_length=200)
    duracao = models.IntegerField(null=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='musicas', null = True)
    letra = models.TextField(default='', null=True, blank=True)
    foto = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField()
    banda = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='albuns', null = True)
    musicas = models.ManyToManyField(Musica, related_name='albuns')
    capa = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nome





