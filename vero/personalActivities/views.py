from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from .forms import *
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def main(request):
  context = {}
  context['form'] = personalActivitiesForm()
  if request.method == 'POST':
    print(request.POST)
  return render(request,"personalActivities/filtroActividadesIndividuales.html", context)

@csrf_exempt
def actividad(request):
  return render(request,"personalActivities/actividad.html")

@csrf_exempt
def recibirActividad(request):
  if request.method == "POST" and request.is_ajax():
    for x in request.POST:
      print(request.POST[x])
    return JsonResponse({"success": True, "respuesta": "siuu"}, status=200)
  return JsonResponse({"success": False, "respuesta": "noou"}, status=400)

