# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from sitenatus.settings import EMAIL_HOST_USER
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from datetime import datetime

from .models import Depoimentos, Servicos, Eventos, Configuracao, Banner, Videos, Contatos, Messages


class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        
        today = datetime.today().date()
        # import ipdb; ipdb.set_trace()
        context['depoiments_list'] = Depoimentos.objects.all()
        context['services_list'] = Servicos.objects.all()
        context['events_list'] = Eventos.objects.filter(data_ini__gte=today).order_by('-id')[0:10]
        context['config'] = Configuracao.objects.all()
        context['banner'] = Banner.objects.all()
        context['videos_list'] = Videos.objects.all().order_by('-id')[0:6]
        return context


def view_send_email(request):
    subject = 'Contato pelo site'
    txt = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    name = request.POST.get('name', '')

    try:
        contato = Contatos.objects.get_or_create(
            email=from_email,
            name=name
        )

        message = Messages.objects.create(
            contact=contato[0],
            text=txt
        )
    except Exception as e:
        print(e)
    
    to_email = [Configuracao.objects.all()[0].email]

    text = """
    
        Mensagem enviada por {nome} - {email}:
    

        {message}

        Obs: Mensagem meramente informativa, não responder.
    """.format(
        nome=name,
        email=from_email,
        message=txt
    )
    try:
        send_mail(
            subject,
            text,
            EMAIL_HOST_USER,
            ["eifmaciel@ucs.br"],
            False
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/')
    