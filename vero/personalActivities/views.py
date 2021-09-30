from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def main(request):
  return render(request,"personalActivities/filtroActividadesIndividuales.html")

def actividad(request):
  return render(request,"personalActivities/actividad.html")
