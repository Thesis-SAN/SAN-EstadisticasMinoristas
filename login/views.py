from django.contrib.auth.forms import AuthenticationForm
from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from platformdirs import user_runtime_dir
from requests import post

# Create your views here.
def san_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if username == '' or password == '':
            context = {
                'form' : form,
                'error': 'Por favor, introduzca un nombre de usuario y clave. Ambos campos son obligatorios.', 
            }
            return TemplateResponse(request,'login.html',context)
        user = authenticate(username=username, password=password, request=request)
        if form.is_valid():
            login(request, form.get_user())

            if user.is_staff:
                login(request, user)
                return HttpResponseRedirect('/dashboard/')##redirect to start page
            