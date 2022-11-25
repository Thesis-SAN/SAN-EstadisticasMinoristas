from django.urls import path
from estad_minoristas.views import index, test, test_table
from login.views import san_login_view

urlpatterns = [
    path('', index),
    path("login/", san_login_view,name = 'login'),
    path("test/", test, name = 'test'),
    path("table/", test_table, name = 'test_table'),
]