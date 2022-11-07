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
from login.forms import MyAuthenticationForm

REDIRECT_FIELD_NAME = 'next'


# Create your views here.
def san_login_view(request,redirect_field_name = REDIRECT_FIELD_NAME):
    if request.method == "POST":
        print('12')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print('is valid')
            login(request, form.get_user())
            return HttpResponseRedirect('/')
    else:
        print(request.method)
        form = AuthenticationForm(request,'/')


    context = {
        'form': form,
        #redirect_field_name: '/',
        'app_path' : request.get_full_path()
    }
    print("path",request.get_full_path())
    return TemplateResponse(request, 'login.html', context)


'''
class MyLoginView(LoginView):
    template_name = 'login.html'
'''

