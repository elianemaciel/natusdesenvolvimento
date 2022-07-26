# -*- coding: UTF-8 -*-
from django.conf import settings
from django.db import models
from django.utils import timezone


class Banner(models.Model):
    titulo = models.CharField(
        max_length=200,
        verbose_name="Titulo"
    )
    descricao = models.CharField(
        max_length=400,
        verbose_name="Frase"
    )
    imagem = models.ImageField(
        upload_to = 'banner/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name="Banner"
        verbose_name_plural = "Banners"


class Depoimentos(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Nome"
    )
    funcao = models.CharField(
        max_length=200,
        verbose_name="Cargo/Função"
    )
    texto = models.TextField(
        verbose_name="Depoimento"
    )

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name="Depoimento"
        verbose_name_plural = "Depoimentos"


class Servicos(models.Model):
    nome = models.CharField(
        max_length=200,
        verbose_name="Titulo"
    )
    metodologia = models.TextField(
        verbose_name="Metodologia"
    )
    icon = models.CharField(
        max_length=50,
        verbose_name="Icone",
        default="ion-ios-paper-outline"
    )
    list_name = models.CharField(
        max_length=200,
        verbose_name="Titulo para check list",
        null=True,
        blank=True
    )
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name="Serviço"
        verbose_name_plural = "Serviços"


class ListServicos(models.Model):
    descricao = models.CharField(max_length=200, verbose_name="Descrição")
    servico = models.ForeignKey(
        Servicos,
        on_delete="SET NULL",
        related_name="list_service"
    )

    class Meta:
        verbose_name="Lista de itens"
        verbose_name_plural = "Listas de itens"


class Eventos(models.Model):
    title = models.CharField(
        max_length=400,
        verbose_name="Titulo"
    )
    descricao = models.TextField(
        verbose_name="Descrição",
        blank=True,
        null=True
    )
    data_ini = models.DateField(
        verbose_name="Data do evento"
    )
    data_fim = models.DateField(
        verbose_name="Data de encerramento",
        null=True,
        blank=True
    )
    horario_ini = models.TimeField(
        verbose_name="Horário de Inicio"
    )
    horario_fim = models.TimeField(
        verbose_name="Horário de Término",
        null=True,
        blank=True
    )
    ministrantes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Ministrantes"
    )
    link = models.URLField(
        max_length=128, 
        db_index=True, 
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to = 'events/',
        blank=True,
        null=True,
        verbose_name="Imagem"
    )

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Evento"
        verbose_name_plural = "Eventos"


class Videos(models.Model):
    descricao = models.CharField(
        max_length=200,
        verbose_name="Titulo"
    )
    iframe = models.TextField(
        verbose_name="iframe",
        help_text="Copie e cole aqui o embed do arquivo",
        blank=True,
        null=True
    )
    file = models.FileField(
        upload_to='videos/',
        null=True,
        blank=True,
        verbose_name="Arquivo - mp4"
    )
    
    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name="Video"
        verbose_name_plural = "Videos"


class Configuracao(models.Model):
    nome_empresa = models.CharField(
        max_length=200,
        verbose_name="Nome da empresa"
    )
    sobre = models.TextField(
        help_text="Sobre a Empresa"
    )
    logo = models.ImageField(
        upload_to = 'settings/',
        blank=True,
        null=True,
        verbose_name="Imagem de logo"
    )
    imagem_fundadora = models.ImageField(
        upload_to = 'settings/',
        blank=True,
        null=True,
        verbose_name="Foto da Fundadora"
    )
    sobre_fundadora = models.TextField(
        verbose_name="Texto sobre a Fundadora"
    )
    frase = models.CharField(
        max_length=300,
        null=True,
        blank=True
    )
    ddd = models.CharField(
        max_length=4,
        verbose_name="DDD",
        help_text="DDD do telefone"
    )
    phone_cel = models.CharField(
        max_length=200,
        verbose_name="Telefone celular/Whatsapp"
    )
    phone_com = models.CharField(
        max_length=200,
        verbose_name="Telefone comercial"
    )
    email = models.EmailField(
        null=True,
        blank=True
    )
    facebook = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    twitter = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    instagram = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    linkedin = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    youtube = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    message_whatsapp = models.CharField(
        max_length=200,
        help_text="Mensagem para iniciar conversa pelo whatsapp"
    )
    rua = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Endereço - Rua"
    )
    numero = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="número da casa"
    )
    cidade = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="Cidade"
    )
    pais = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="País"
    )
    video_institucional = models.TextField(
        verbose_name="Vide Institucional",
        help_text="Copie e cole aqui o embed do arquivo",
        blank=True,
        null=True
    )
    created_date = models.DateTimeField(default=timezone.now)

    @property
    def get_whatssapp_number(self):
        return "+55" + str(self.ddd) + str(self.phone_cel)


    def __str__(self):
        return self.nome_empresa
    
    class Meta:
        verbose_name="Configuração do Site"
        verbose_name_plural = "Configurações"


class Contatos(models.Model):
    email = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name="Contato"
        verbose_name_plural = "Contatos"


class Messages(models.Model):
    contact = models.ForeignKey(
        Contatos,
        on_delete="SET NULL",
        related_name="messages"
    )
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.contact.name

    class Meta:
        verbose_name="Mensagem"
        verbose_name_plural = "Mensagens"


class Certificados(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=200
    )
    imagem = models.ImageField(
        upload_to = 'certificates/',
        blank=True,
        null=True,
        verbose_name="Imagem/logo da certificação"
    )
    text = models.TextField(
        blank=True,
        null=True,
    )
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name="Certificado"
        verbose_name_plural = "Certificados"
        
class Menus(models.Model):
    nome = models.CharField(
        verbose_name="Nome",
        max_length=200
    )
    
    ordem = models.IntegerField(
        verbose_name="Ordem"
    )
    
    href = models.CharField(
        verbose_name="Link",
        max_length=200
    )
    