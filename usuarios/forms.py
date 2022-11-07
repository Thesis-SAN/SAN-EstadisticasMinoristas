from django import forms
from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from usuarios.models import Usuario


class usuariosForm(forms.ModelForm):
    attrs_user = {
        'class': 'form-control input-circle',
         'style': 'margin-bottom: 15px'
    }
    attrs_pass = {
        "type": "password",
        'class': 'form-control input-circle',
        'style': 'margin-bottom: 15px'
    }
    
    usuario = forms.CharField(max_length=250,required=True,label='Usuario', widget=forms.TextInput(attrs=attrs_user))
    password = forms.CharField(widget=forms.TextInput(attrs=attrs_pass))
    
    class Meta:
        model = Usuario
        fields = ('usuario','password')