from django.conf import settings
from django.db import models
from django.utils import timezone

class Banner(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=400)
    imagem = models.ImageField(upload_to = 'banner/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name="Banner"
        verbose_name_plural = "Banners"


class Depoimentos(models.Model):
    nome = models.CharField(max_length=200)
    funcao = models.CharField(max_length=200)
    texto = models.TextField()
    image = models.ImageField(blank=True, null=True)

    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name="Depoimento"
        verbose_name_plural = "Depoimentos"


class Servicos(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Titulo",)
    metodologia = models.TextField(verbose_name="Metodologia")
    icon = models.CharField(
        max_length=50, verbose_name="Icone", default="ion-ios-paper-outline")
    list_name = models.CharField(max_length=200, verbose_name="Titulo para check list", null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name="Serviço"
        verbose_name_plural = "Serviços"


class ListServicos(models.Model):
    descricao = models.CharField(max_length=200)
    servico = models.ForeignKey(Servicos, on_delete="SET NULL", related_name="list_service")

    class Meta:
        verbose_name="Lista de itens"
        verbose_name_plural = "Listas de itens"


class Eventos(models.Model):
    title = models.CharField(max_length=400, verbose_name="Titulo")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    data_ini = models.DateField(verbose_name="Data do evento")
    data_fim = models.DateField(verbose_name="Data de encerramento", null=True, blank=True)
    horario_ini = models.TimeField(verbose_name="Horário de Inicio")
    horario_fim = models.TimeField(verbose_name="Horário de Término", null=True, blank=True)
    ministrantes = models.TextField(blank=True, null=True)
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
    
    class Meta:
        verbose_name="Evento"
        verbose_name_plural = "Eventos"

class Videos(models.Model):
    descricao = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        verbose_name="Lista de itens"
        verbose_name_plural = "Listas de itens"


class Configuracao(models.Model):
    nome_empresa = models.CharField(max_length=200)
    sobre = models.TextField(help_text="Sobre a Empresa")
    logo = models.ImageField(upload_to = 'settings/', blank=True, null=True)
    imagem_fundadora = models.ImageField(upload_to = 'settings/', blank=True, null=True)
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

    @property
    def get_whatssapp_number(self):
        return "+55" + str(self.ddd) + str(self.phone_cel)


    def __str__(self):
        return self.nome_empresa
    

    class Meta:
        verbose_name="Configuração do Site"
        verbose_name_plural = "Configurações"
