from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from .models import ActivityType, ActivityCategory, PersonalActivites

# Create your views here.
@login_required(login_url='/users/login/')
def temp(request):
  all_activities = PersonalActivites.objects.order_by('-pub_data')
  context = {
    "pageTitle": "Personal Activities list",
    "activities": all_activities
  }


  return render(request, "personalActivities/personalActivitiesList.html", context)


@login_required(login_url='/users/login/')
def singleActivity(request, activity_id):
  activity = get_object_or_404(PersonalActivites, pk=activity_id)
  context = {
    "activity" : activity
  }
  return render(request, "personalActivities/activity.html", context)


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



