from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils import timezone

from .models import ActivityType, ActivityCategory, PersonalActivites
from users.models import User_activity
from encuesta.models import Encuesta

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
def singleActivity(request, activity_id):
    user_activity = User_activity.objects.get(pk=activity_id)
    context = {
        "activity": user_activity.activity,
        "user_activity_id": user_activity.id
    }
    return render(request, "personalActivities/actividad.html", context)


@login_required(login_url='/users/login/')
def singleActivity_selection(request, activity_id):
    activity = PersonalActivites.objects.get(id=activity_id)
    user_profile = request.user.user_profile
    try:  # el usuario ya inicio la actividad pero no la ha finalizado
        user_activity = User_activity.objects.get(
            user=user_profile, activity=activity, status='started')

    except User_activity.DoesNotExist as e:
        encuesta = Encuesta(sentimientoInicial="", sentimientoFinal="")
        encuesta.save()
        user_activity = User_activity(
            user=user_profile, activity=activity, encuesta=encuesta)
        user_activity.save()

    return redirect('encuestaAntes', activity_id=user_activity.id)


@login_required(login_url='/users/login/')
def singleActivity_finish(request, activity_id):
    try:  # el usuario ya inicio la actividad pero no la ha finalizado
        user_activity = User_activity.objects.get(pk=activity_id)

        user_activity.date_finish = timezone.now()
        user_activity.status = 'finish'
        user_activity.save()
    except User_activity.DoesNotExist as e:
        print(e)

    return redirect('encuesta', activity_id=user_activity.id)
