"""djproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app_intro.views import index
 

urlpatterns = [
    # include do arquivo de urls da aplicação "artigo"
    path('artigos/', include('artigo.urls')),
    path('admin/', admin.site.urls),
    #path('form', TemplateView.as_view(template_name='index.html')),
    #path('print_req_get', print_get,name='print_get'),
    #path('print_req_post', print_post, name='print_post'),
    path('', index, name='index'),
    #path('form/', form, name='form'),

]