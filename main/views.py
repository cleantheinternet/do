from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response

def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(request))


def publishers(request):
    template = loader.get_template('main/publishers.html')
    return HttpResponse(template.render(request))


def companies(request):
    template = loader.get_template('main/companies.html')
    return HttpResponse(template.render(request))


def about(request):
    template = loader.get_template('main/about.html')
    return HttpResponse(template.render(request))



