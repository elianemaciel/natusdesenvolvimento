from django.contrib import admin
from .models import Videos, Configuracao, Servicos, ListServicos, Eventos, Depoimentos, Banner, Contatos, Messages

class ConfigAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados da Empresa', {
            'fields': ('nome_empresa', ('ddd', 'phone_cel', 'phone_com'), 'email',('rua', 'numero', 'cidade', 'pais')),
        }),
        ('Sobre', {
            'fields': ('sobre', 'logo', 'imagem_fundadora', 'sobre_fundadora', 'frase'),
        }),
        ('Social', {
            'fields': ('facebook', 'twitter', 'instagram', 'message_whatsapp'),
        }),
    )

class ListServicosAdmin(admin.TabularInline):
    model = ListServicos

class ServicosAdmin(admin.ModelAdmin):
   inlines = [ListServicosAdmin,]


admin.site.register(Configuracao, ConfigAdmin)
admin.site.register(Eventos)
admin.site.register(Servicos, ServicosAdmin)
admin.site.register(Depoimentos)
admin.site.register(Banner)
admin.site.register(Videos)
admin.site.register(Messages)
admin.site.register(Contatos)

admin.site.site_header = 'Natus Desenvolvimento Humano e Organizacional - Administração'