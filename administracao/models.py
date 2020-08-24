from django.conf import settings
from django.db import models
from django.utils import timezone

class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    imagem = models.ImageField()

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
    sobre = models.TextField(help_text="Sobre a Empresa")
    logo = models.ImageField()
    imagem_fundadora = models.ImageField()
    sobre_fundadora = models.TextField()
    frase = models.CharField(max_length=300, null=True, blank=True)
    ddd = models.CharField(max_length=4)
    phone_cel = models.CharField(max_length=200)
    phone_com = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    message_whatsapp = models.CharField(
        max_length=200,
        help_text="Mensagem para iniciar conversa pelo whatsapp"
    )
    rua = models.CharField(max_length=200, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    cidade = models.CharField(max_length=200, null=True, blank=True)
    pais = models.CharField(max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome_empresa