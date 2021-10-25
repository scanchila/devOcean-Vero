from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from .models import ActivityType, ActivityCategory, PersonalActivites, EventRegisterForm

# Create your views here.
@login_required(login_url='/users/login/')
def main(request):
  all_activities = PersonalActivites.objects.order_by('-pub_data')
  act_name = ActivityCategory.objects.all()
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


def recibirActividad(request):
  if request.method == "POST" and request.is_ajax():
    #for x in request.POST:
    #  print(request.POST[x])
    return JsonResponse({"success": True, "respuesta": "siuu"}, status=200)
  return JsonResponse({"success": False, "respuesta": "noou"}, status=400)

@login_required(login_url='/users/login/')
def formEvent(request):
    context = {
        'pageTitle' : 'CreateEvent',
    }
    if request.method == 'POST':
        form = EventRegisterForm(request.POST)
        if form.is_valid():
            form.save()
    context['form'] = form
    return render(request,  'personalActivities/activity.html', context)