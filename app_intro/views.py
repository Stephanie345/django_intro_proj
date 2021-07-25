"""from django.shortcuts import render

# Create your views here.

enderfrom django.http import HttpResponsedef print_reqs(request):print (request)return HttpResponse('hello world')
# app_intro/views.py - django_necto_fatec/django_intro_proj/djproj/app_intro/views.pyfrom django.shortcuts import r
"""

# app_intro/views.py
from django.shortcuts import render
from django.http import HttpResponse
 

from django.views.decorators.csrf import csrf_exempt
 
@csrf_exempt
def print_reqs(request):

    '''
    imprime requisiçoes
    '''
 
    #print ("\n-------POST--------------\n")
    #print (request.POST)
    print ("\n-------POST--------------\n")
    print (request.GET)
    # print ("\n-------REQUEST--------------\n")
    # print(dir(request))
    # print ("\n-------META--------------\n")
    # print(request.META)
 
    return HttpResponse('funcionou!','index.html')

def index(request):
    template_name =  'index_template.html'
    return render(request, template_name, context=None, content_type=None, status=None, using=None)