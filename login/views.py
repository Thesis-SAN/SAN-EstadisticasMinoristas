from site import execsitecustomize
from django.contrib.auth.forms import AuthenticationForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from platformdirs import user_runtime_dir
from requests import post
from usuarios.models import Usuario
from django.shortcuts import redirect

REDIRECT_FIELD_NAME = 'next'

# Create your views here.
def san_login_view(request,redirect_field_name = REDIRECT_FIELD_NAME):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)#binding data to form
        username = request.POST['username']
        password = request.POST['password']

        if username == '' or password == '':
            context = {
                'form' : form,
                'error': 'Por favor, introduzca un nombre de usuario y clave. Ambos campos son obligatorios.', 
            }
            return TemplateResponse(request,'login.html',context)

        #authenticate: verify username and password
        user = authenticate(username=username, password=password, request=request)

        if form.is_valid():# runs validation routines for all its fields
            #asocia usuario a la sesion actual
            login(request, form.get_user())
            return HttpResponseRedirect('')##redirect to start page

        else:
            context = {
                'form': form,
                'error': 'Por favor, introduzca un nombre de usuario y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas.',
            }
            return TemplateResponse(request, 'login.html', context)
    
    #method=GET
    else:
        form = AuthenticationForm(request)

    context = {
        'form': form,
        redirect_field_name: 'index.html',
    }

    return TemplateResponse(request, 'login.html', context)
    