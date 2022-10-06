from django.urls import path
from estad_minoristas.views import index

urlpatterns = [
    path('', index),
]