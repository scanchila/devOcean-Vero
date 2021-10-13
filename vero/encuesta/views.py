from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
  return render(request,"encuesta/encuestaAntes.html")

def encuestaDespues(request):
  return render(request,"encuesta/encuesta.html")
