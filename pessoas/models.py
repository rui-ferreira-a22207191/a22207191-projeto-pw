from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    apelido = models.CharField(max_length=200)
    idade = models.IntegerField()

    def __str__(self):
        return f"Nome: {self.nome} | Apelido: {self.apelido} | Idade: {self.idade}"