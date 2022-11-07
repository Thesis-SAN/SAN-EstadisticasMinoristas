from django.urls import path
from estad_minoristas.views import index, login
from login.views import san_login_view

urlpatterns = [
    path('', index),
    path("login/", san_login_view,name = 'login'),
]