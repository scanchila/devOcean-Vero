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
def main(request):
  all_activities = PersonalActivites.objects.order_by('-pub_data')
  act_name = ActivityType.objects.all()
  context = {
    "pageTitle": "Personal Activities list",
    "activities": all_activities,
    "act_name": act_name
  }

  return render(request, "personalActivities/filtroActividadesIndividuales.html", context)


@login_required(login_url='/users/login/')
def singleActivity(request, activity_id):
  activity = get_object_or_404(PersonalActivites, pk=activity_id)
  context = {
    "activity" : activity
  }
  return render(request, "personalActivities/actividad.html", context)

@login_required(login_url='/users/login/')
def recibirActividad(request):
  context = {}
  if request.method == "POST":
    activities = None
    if request.POST["resource"] == "any" and request.POST["time"] == "any" and request.POST["act_type"] == "any":
      activities = PersonalActivites.objects.order_by('-pub_data')
    elif request.POST["resource"] == "any" and request.POST["time"] == "any" and request.POST["act_type"] != "any":
      act_type = request.POST["act_type"]
      activities = PersonalActivites.objects.raw("select * from personalActivities_personalactivites "
                                                 "where (select id from personalActivities_activitytype "
                                                 f"where name = '{act_type}') = "
                                                 "activityType_id")

    act_name = ActivityType.objects.all()
    context = {
      "pageTitle": "Personal Activities list",
      "activities": activities,
      "act_name": act_name
    }

  return render(request, "personalActivities/filtroActividadesIndividuales.html", context)




