from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from encuesta.models import Encuesta
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/users/login/')
def index(request, activity_id):
  context = {
    'activity_id' : activity_id
  }
  return render(request,"encuesta/encuestaAntes.html", context)

@login_required(login_url='/users/login/')
def encuestaDespues(request):
  return render(request,"encuesta/encuesta.html")

@csrf_exempt
def recibirEncuesta(request):
  #if request.method=="POST" and request.is_ajax():
  #  print(request.POST["sentimientoInicial"])
  #  return JsonResponse({"success": True, "respuesta": "siuu"}, status=200)
  print(request.COOKIES['username'])
  user=User.objects.get(username=request.COOKIES['username'])
  if request.method == 'POST'and request.is_ajax():
    print("Vegetableeeees")
    form = Encuesta(request.POST)
    form = Encuesta(user=user,sentimientoInicial=request.POST["sentimientoInicial"],sentimientoFinal=request.POST["sentimientoFinal"])
    form.save()
  else:
    form = Encuesta()
  return JsonResponse({"success": False, "respuesta": "noou"}, status=400)

