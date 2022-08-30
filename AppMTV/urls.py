from django.urls import path
from AppMTV.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('familiares', familiares, name='familiares'),
]