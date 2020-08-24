from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

from .models import Depoimentos, Servicos, Eventos, Configuracao, Banner


class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['depoiments_list'] = Depoimentos.objects.all()
        context['services_list'] = Servicos.objects.all()
        context['events_list'] = Eventos.objects.all()
        context['config'] = Configuracao.objects.all()
        context['banner'] = Banner.objects.all()
        return context

def send_email(request):
    subject = 'Teste'
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    # to_email = [Configuracao.objects.all()[0].email]
    to_email = ["eliane.faveron@gmail.com"]
    if subject and message and from_email:
        try:
            send_email(subject, message, from_email, ["eifmaciel@ucs.br"])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')