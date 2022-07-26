# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.views.generic import ListView

from datetime import datetime

from sitenatus.settings import EMAIL_HOST_USER
from .models import Depoimentos, Menus, Servicos, Eventos, Configuracao, Banner, Videos, Contatos, Messages, Certificados


class HomeView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        
        today = datetime.today().date()
        context['depoiments_list'] = Depoimentos.objects.all()
        context['services_list'] = Servicos.objects.all()
        context['events_list'] = Eventos.objects.filter(data_ini__gte=today).order_by('-id')[0:10]
        context['config'] = Configuracao.objects.all()[0]
        context['banner'] = Banner.objects.all()
        context['videos_list'] = Videos.objects.all().order_by('-id')[0:6]
        context['menus'] = Menus.objects.all().order_by('ordem')
        context['certificates'] = Certificados.objects.all()
        return context


class ListVideosView(ListView):
    model = Videos
    template_name = "videos_list.html"


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
    emails = []
    to_email = Configuracao.objects.all()[0].email
    emails.append(to_email)

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
            emails,
            False
        )
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return HttpResponseRedirect('/')
    