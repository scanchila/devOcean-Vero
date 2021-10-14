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
    return redirect("menu")
  
  context = {
    'pageTitle' : 'Landing'
  }
  return render(request,"home/landing.html", context)


def menu(request):
  pers = PersonalActivites.objects.all()
  data = serialize('json', pers)
  data = json.loads(data)
  context = {
    'activities': [[x.name, x.description, x.image_URL, x.duration] for x in pers]
  }
  return render(request, "home/menu.html", context=context)


@csrf_exempt
def traerActividades(request):
  if request.method == 'POST':#:
    print("Vegetableeeees")
    pers = PersonalActivites.objects.all()
    data = serialize('json',pers)
    data = json.loads(data)
    context = {
      'activities': data
    }
    return render(request, context=context)
  return render(request, context={'status':400})
