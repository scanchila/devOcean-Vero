from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.core.serializers import serialize
from personalActivities.models import PersonalActivites


# Create your views here.
def index(request):
  if(request.user.is_authenticated):
    return redirect("personal_activities_list")
  
  context = {
    'pageTitle' : 'Landing'
  }
  return render(request,"home/landing.html", context)

@csrf_exempt
def traerActividades(request):
  if request.method == 'POST':#:
    print("Vegetableeeees")
    pers = PersonalActivites.objects.all()
    data = serialize('json',pers)
    data = json.loads(data)
    return JsonResponse({"success": True, "respuesta": data}, status=200)
  return JsonResponse({"success": False, "respuesta": "noou"}, status=400)