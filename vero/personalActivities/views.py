from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def main(request):
  f = open('personalActivities/ActivityGroup.json',)
  data = json.load(f)
  dat = []
  for i in data['activities']:
    dat.append(i)
  f.close()
  return render(request,"personalActivities/filtroActividadesIndividuales.html", context={'data':data})

def actividad(request):
  return render(request,"personalActivities/actividad.html")

def recibirActividad(request):
  if request.method == "POST" and request.is_ajax():
    #for x in request.POST:
    #  print(request.POST[x])
    return JsonResponse({"success": True, "respuesta": "siuu"}, status=200)
  return JsonResponse({"success": False, "respuesta": "noou"}, status=400)



