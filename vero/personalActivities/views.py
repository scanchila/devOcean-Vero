from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


from .models import ActivityType, ActivityCategory, PersonalActivites
from users.models import User_activity

# Create your views here.


@login_required(login_url='/users/login/')
def main(request):
    all_activities = PersonalActivites.objects.order_by('-pub_data')
    f = open('personalActivities/ActivityGroup.json',)
    data = json.load(f)
    dat = []
    for i in data['activities']:
        dat.append(i)
    f.close()
    context = {
        "pageTitle": "Personal Activities list",
        "activities": all_activities,
        'data': data
    }

    return render(request, "personalActivities/filtroActividadesIndividuales.html", context)


@login_required(login_url='/users/login/')
def singleActivity(request, activity_id, feeling=""):
    activity = get_object_or_404(PersonalActivites, pk=activity_id)
    user_profile = request.user.user_profile
    user_activity = User_activity.objects.get(
        user=user_profile, activity=activity)

    encuesta = user_activity.encuesta
    encuesta.sentimientoInicial = feeling
    encuesta.save()
    context = {
        "activity": activity
    }
    return render(request, "personalActivities/actividad.html", context)


def recibirActividad(request):
    if request.method == "POST" and request.is_ajax():
        # for x in request.POST:
        #  print(request.POST[x])
        return JsonResponse({"success": True, "respuesta": "siuu"}, status=200)
    return JsonResponse({"success": False, "respuesta": "noou"}, status=400)
