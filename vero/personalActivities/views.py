from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import datetime

from .models import ActivityType, ActivityCategory, PersonalActivites
from users.models import User_activity
from encuesta.models import Encuesta


# Create your views here.


@login_required(login_url='/users/login/')
def main(request):
    all_activities = PersonalActivites.objects.order_by('-pub_data')
    act_cat = ActivityCategory.objects.all()
    act_type = ActivityType.objects.all()
    context = {
        "pageTitle": "Personal Activities list",
        "activities": all_activities,
        "act_type": act_type,
        "act_cat": act_cat
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
def recibirActividad(request):
    context = {}
    if request.method == "POST":
        activities = set()
        actTime = None
        actType = None
        actCategory = None

        if request.POST["time"] != "any":
            args = request.POST["time"].split(",")
            actTime = PersonalActivites.objects.filter(duration__gte=datetime.timedelta(minutes=int(args[0])),
                                                       duration__lte=datetime.timedelta(minutes=int(args[1])))

        if request.POST["act_type"] != "any":
            a_type = request.POST["act_type"]
            tipo = ActivityType.objects.get(id=a_type)
            actType = tipo.personalactivites_set.all()

        if request.POST["category"] != "any":
            a_cat = request.POST["category"]
            category = ActivityCategory.objects.get(id=a_cat)
            actCategory = category.personalactivites_set.all()

        if request.POST["category"] == "any" and request.POST["time"] == "any" and request.POST["act_type"] == "any":
            activities = PersonalActivites.objects.order_by('-pub_data')
        else:
            if actTime and actType and actCategory:
                activities = set(actTime).intersection(
                    set(actType)).intersection(actCategory)
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


def dashboard_admin(request):

    return render(request, "personalActivities/dashboard.html")
