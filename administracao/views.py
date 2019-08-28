from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Depoimentos, Servicos, Eventos, Configuracao

class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['depoiments_list'] = Depoimentos.objects.all()
        context['services_list'] = Servicos.objects.all()
        context['events_list'] = Eventos.objects.all()
        context['config'] = Configuracao.objects.get_or_create(id=2)
        return context