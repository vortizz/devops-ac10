"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from app.models import Curso, Vestibular, Candidato
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contato',
            'message':'Entre em contato conosco',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Gerenciador de vestibulares',
            'year':datetime.now().year,
        })
    )

def cadastro_cursos(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/cadastro_cursos.html',
        context_instance = RequestContext(request,
        {
            'title':'Cadastro de cursos',
#            'cursos': ['ADS' , 'SI', 'CC'],
            'cursos': Curso.objects.all(),
            'year':datetime.now().year,
        })
    )
def cadastro_vestibulares(request): 
     assert isinstance(request, HttpRequest) 
     return render(
     request,
    'app/cadastro_vestibulares.html', 
     context_instance = RequestContext(request,
     {
     'title':'Cadastro de vestibulares',
     'vestibulares': Vestibular.objects.all( ),
     'year':datetime.now().year, 
     })
)

def cadastro_candidatos(request): 
     assert isinstance(request, HttpRequest) 
     return render(
     request,
    'app/cadastro_candidatos.html', 
     context_instance = RequestContext(request,
     {
     'title':'Cadastro de candidatos',
     'candidatos': Candidato.objects.all( ),
     'year':datetime.now().year, 
     })
)
