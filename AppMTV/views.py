from django.shortcuts import render
from .models import Familiar

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def familiares(request):
    familiar1 = Familiar(nombre="Marcos Catrini", edad=62, fechaDeNacimiento='1960-05-09', profesion="Administrador público")
    familiar2 = Familiar(nombre="Patricia Fernández", edad=60, fechaDeNacimiento='1962-01-19', profesion="Administradora público")
    familiar3 = Familiar(nombre="Brenda Catrini", edad=27, fechaDeNacimiento='1994-09-28', profesion="Docente")
    familiar1.save()
    familiar2.save()
    familiar3.save()
    lista = [familiar1, familiar2, familiar3]
    return render(request, "familiares.html", {'lista':lista})

