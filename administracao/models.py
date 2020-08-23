from django.conf import settings
from django.db import models
from django.utils import timezone


class Depoimentos(models.Model):
    nome = models.CharField(max_length=200)
    funcao = models.CharField(max_length=200)
    texto = models.TextField()
    image = models.ImageField()

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Servicos(models.Model):
    nome = models.CharField(max_length=200)
    metodologia = models.TextField()
    icon = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class Eventos(models.Model):
    title = models.CharField(max_length=400)
    descricao = models.TextField()
    data_ini = models.DateField()
    data_fim = models.DateField()
    horario_ini = models.TimeField()
    horario_fim = models.TimeField()
    link = models.URLField(
        max_length=128, 
        db_index=True, 
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to = 'events/', blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Configuracao(models.Model):
    nome_empresa = models.CharField(max_length=200)
    sobre = models.TextField()
    sobre_fundadora = models.TextField()
    valores = models.TextField()
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