from django.db import models

# Create your models here.

class AreaCientifica1(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class LinguagemProgramacao1(models.Model):
    nome = models.CharField(max_length=25)

    def __str__(self):
        return self.nome


class Docente1(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null= True)
    def __str__(self):
        return self.nome

class Cadeira1(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    semestre = models.CharField(max_length=20)
    ects = models.IntegerField()
    tempo = models.IntegerField()
    prof = models.ManyToManyField(Docente1, related_name="cadeiras")

    def __str__(self):
        return self.nome

class Projeto1(models.Model):
    nome = models.CharField(max_length=100)
    description = models.TextField()
    autor = models.CharField(max_length=100)
    video = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    linguagens = models.ManyToManyField(LinguagemProgramacao1,related_name="projetos")
    cadeira = models.ForeignKey(Cadeira1, on_delete=models.CASCADE,null = True, related_name="cadeira")

    def __str__(self):
        return self.nome

class Curso1(models.Model):
    nome = models.CharField(max_length=100)
    ects = models.IntegerField()
    bio = models.TextField()
    competencia = models.TextField()
    semestres = models.IntegerField()
    departamento = models.CharField(max_length=100)
    secretario = models.CharField(max_length=100)
    tempo = models.CharField(max_length=100)
    areaCientifica = models.ForeignKey(AreaCientifica1, on_delete=models.CASCADE, related_name="cursos")
    cadeiras = models.ManyToManyField(Cadeira1, related_name="cursos")

    def __str__(self):
        return self.nome
