from django.urls import path
from estad_minoristas.views import index, login

urlpatterns = [
    path('', index),
    path("login/", login),
]