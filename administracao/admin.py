from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Configuracao)
admin.site.register(Eventos)
admin.site.register(Servicos)
admin.site.register(Depoimentos)

admin.site.site_header = 'Natus Desenvolvimento Administração'