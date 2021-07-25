from django.shortcuts import render
from django.http import HttpResponse

def artigo_ultimos(request):
    return HttpResponse('<h1>artigos ultimos</h1>')
def artigo_pagina(request, pag=1):
    return HttpResponse('<h1>artigos pagina</h1>')
def artigo_ano(request, ano=2021):
    return HttpResponse('<h1>artigo ano</h1>')
