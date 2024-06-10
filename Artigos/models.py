from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class MeuUsuario(models.Model):
    nome = models.CharField(max_length=150)
    foto_perfil = models.ImageField(upload_to='fotos_perfil', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil', blank=True, null=True)
    sobre = models.TextField(default='', blank=True, null=True)
    rede_social = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome
class Artigo(models.Model):
    DESPORTO = 'Desporto'
    ECONOMIA = 'Economia'
    TECNOLOGIA = 'Tecnologia'
    NOTICIAS_MUNDO = 'Noticias Mundo'

    GENERO_CHOICES = [
        (DESPORTO, 'Desporto'),
        (ECONOMIA, 'Economia'),
        (TECNOLOGIA, 'Tecnologia'),
        (NOTICIAS_MUNDO, 'Noticias Mundo'),
    ]

    titulo = models.CharField(max_length=50)
    data_publicacao = models.DateTimeField(blank=True, null=True)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='artigos')
    link = models.URLField(blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='artigos')
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    titulo = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comentarios', null=True)
    data = models.DateTimeField()
    texto = models.TextField()

    MAU = 1
    NORMAL = 2
    BOM = 3
    EXCELENTE = 4
    AVALIACAO_CHOICES = [
        (MAU, "Mau"),
        (NORMAL, "Normal"),
        (BOM, "Bom"),
        (EXCELENTE, "Excelente"),
    ]

    avaliacao = models.IntegerField(choices=AVALIACAO_CHOICES)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios', null=True)

    def __str__(self):
        return self.titulo








