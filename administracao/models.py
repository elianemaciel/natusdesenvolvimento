from django.conf import settings
from django.db import models
from django.utils import timezone


class Depoimentos(models.Model):
    nome = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Servicos(models.Model):
    nome = models.CharField(max_length=200)
    metodologia = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Eventos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_ini = models.DateField()
    data_fim = models.DateField()
    horario_ini = models.TimeField()
    horario_fim = models.TimeField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Configuracao(models.Model):
    nome_empresa = models.CharField(max_length=200)
    sobre = models.TextField()
    valor = models.TextField()
    phone_cel = models.CharField(max_length=200)
    phone_com = models.CharField(max_length=200)
    email = models.EmailField()
    localizacao = models.TextField()
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_empresa