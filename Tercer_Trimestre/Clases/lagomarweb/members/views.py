from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirsthtml.html')
  return HttpResponse(template.render())

def aboutme(request):
  template = loader.get_template('myfirsthtml.html')
  termino = request.GET.get('texto')
  return HttpResponse(template.render({"name": str(termino)}))

def sign_in(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())