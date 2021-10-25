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
    activities = set()

    actTime = None
    actType = None
    actCategory = None
    if request.POST["time"] != "any":
      args = request.POST["time"].split(",")
      query = f"select * from personalActivities_personalactivites " \
              f"where duration <= {int(args[1]) * 1000000} and duration >= {int(args[0]) * 1000000}"
      actTime = PersonalActivites.objects.raw(query)

    if request.POST["act_type"] != "any":
      a_type = request.POST["act_type"]
      query = f"select * from personalActivities_personalactivites " \
              f"where (select id from personalActivities_activitytype " \
              f"where name = '{a_type}') = activityType_id"
      actType = PersonalActivites.objects.raw(query)

    if request.POST["category"] != "any":
      a_cat = request.POST["category"]
      query = "select personalActivities_personalactivites.id, personalActivities_personalactivites.name, " \
              "personalActivities_personalactivites.description, personalActivities_personalactivites.image_URL, " \
              "personalActivities_personalactivites.lecture, personalActivities_personalactivites.pub_data, " \
              "personalActivities_personalactivites.duration, personalActivities_personalactivites.activityType_id, " \
              "personalActivities_personalactivites.video_URL " \
              "from personalActivities_personalactivites, personalActivities_personalactivites_categories, " \
              "personalActivities_activitycategory " \
              "where personalActivities_personalactivites.id = personalActivities_personalactivites_categories.personalactivites_id " \
              f"and personalActivities_personalactivites_categories.activitycategory_id = (select id from personalActivities_activitycategory where name = '{a_cat}');"
      actCategory = PersonalActivites.objects.raw(query)



    if request.POST["category"] == "any" and request.POST["time"] == "any" and request.POST["act_type"] == "any":
      activities = PersonalActivites.objects.order_by('-pub_data')
    else:
      if actTime and actType and actCategory:
        activities = set(actTime).intersection(set(actType)).intersection(actCategory)
      if actTime and actType:
        activities = set(actTime).intersection(set(actType))
      elif actTime and actCategory:
        activities = set(actTime).intersection(set(actCategory))
      elif actType and actCategory:
        activities = set(actType).intersection(set(actCategory))
      elif actTime:
        activities = actTime
      elif actType:
        activities = actType
      elif actCategory:
        activities = actCategory





    act_cat = ActivityCategory.objects.all()
    act_type = ActivityType.objects.all()
    context = {
      "pageTitle": "Personal Activities list",
      "activities": activities,
      "act_type": act_type,
      "act_cat": act_cat
    }

  return render(request, "personalActivities/filtroActividadesIndividuales.html", context)




