from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput, TextInput

class MyAuthenticationForm(AuthenticationForm):
    username =  forms.CharField(widget=TextInput(attrs={'class':'form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8','type':"text", 'placeholder':"Username", 'name':"username", 'autocomplete':"off"}))#forms.TextInput(widget={'class':'form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8', 'type':"text", 'placeholder':"Username", 'name':"username", 'autocomplete':"off" })
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8', 'type':"password", 'placeholder':"Password", 'name':"password"}))#forms.TextInput(widget={'class':'form-control h-auto text-white bg-white-o-5 rounded-pill border-0 py-4 px-8', 'type':"password", 'placeholder':"Password", 'name':"password"})
    
