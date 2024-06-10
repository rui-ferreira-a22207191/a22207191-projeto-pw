from django.db import models

class Banda(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200, null = True)
    anoCriacao = models.IntegerField()
    foto = models.ImageField(null = True)

    def __str__(self):
        return self.nome

class Musica(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField()
    link = models.URLField(max_length=200)
    duracao = models.IntegerField(null=True)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='musicas', null = True)
    letra = models.TextField(null = True)

    def __str__(self):
        return self.nome

class Album(models.Model):
    nome = models.CharField(max_length=200)
    ano_lancamento = models.IntegerField()
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE, related_name='albuns', null = True)
    musicas = models.ManyToManyField(Musica, related_name='albuns')
    capa = models.ImageField()

    def __str__(self):
        return self.nome





