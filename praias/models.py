from django.db import models

# Create your models here.



class Regiao(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome



class Praia(models.Model):
    nome = models.CharField(max_length=200)
    imagem = models.ImageField(upload_to='praias')
    servico  = models.ManyToManyField(Servico,related_name='praias')
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name='praias')

    def __str__(self):
        return self.nome

