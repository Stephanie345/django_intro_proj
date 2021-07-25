# arquivo: django_necto_fatec/django_intro_proj/djproj/artigo/urls.py
from django.urls import path, re_path
from . import views
# as urls abaixo são inclusas no djproj/urls.py
# então a URL = "artigos/<url_definida_aqui>
urlpatterns = [
# ex.: http://127.0.0.1:8000/artigos/
# na view
path('', views.artigo_ultimos, name="artigos_ultimos"),
# ex.: http://127.0.0.1:8000/artigos/pagina/2/
# na view -> def page(request, num=1):
path('pagina/<int:pag>/', views.artigo_pagina, name="artigos_pagina"),
# ex.: http://127.0.0.1:8000/artigos/2022/
# envia o parametro ano, definido na regex
re_path(r'^(?P<ano>[0-9]{4})/$', views.artigo_ano, name="artigos_ano"),
]