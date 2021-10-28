from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
import datetime

from .models import ActivityType, ActivityCategory, PersonalActivites
from users.models import User_activity
from encuesta.models import Encuesta
from .dashboard import *


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
        activities = PersonalActivites.objects.all()

        if request.POST["time"] != "any":
            args = request.POST["time"].split(",")
            activities = activities.filter(duration__gte=datetime.timedelta(
                minutes=int(args[0])), duration__lte=datetime.timedelta(minutes=int(args[1])))

        if request.POST["act_type"] != "any":
            a_type = request.POST["act_type"]
            activities = activities.filter(activityType_id=a_type)

        if request.POST["category"] != "any":
            a_cat = request.POST["category"]
            activities = activities.filter(categories__in=[a_cat])

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


@login_required(login_url='/users/login/')
@staff_member_required
def dashboard(request):
    context = {
        'pageTitle': 'dashboard'
    }
    return render(request, 'personalActivities/dashboard.html', context)


@login_required(login_url='/users/login/')
@staff_member_required
def dashboard_charts(request, chart):

    context = {}
    if chart == 'activities':
        context = {
            'title': 'Actividades mas realizadas',
            'data': {
                'labels': [c.name[:25] for c in most_view_activities()],
                'datasets': [{
                    'label': 'Total',
                    'data': [{'x': c.name[:25], 'y': c.num_ua} for c in most_view_activities()],
                }, {
                    'label': 'Sin terminar',
                    'data': [{'x': c.name[:25], 'y': c.num_ua} for c in most_view_activities('started')],
                }, {
                    'label': 'Terminadas',
                    'data': [{'x': c.name[:25], 'y': c.num_ua} for c in most_view_activities('finish')]
                }]
            }
        }

    elif chart == 'types':
        context = {
            'title': 'Tipos de actividades mas realizadas',
            'data': {
                'labels': [c.name for c in groupby_type()],
                'datasets': [{
                    'label': 'Total',
                    'data': [{'x': c.name, 'y': c.num_ua} for c in groupby_type()],
                }, {
                    'label': 'Sin terminar',
                    'data': [{'x': c.name, 'y': c.num_ua} for c in groupby_type('started')],
                }, {
                    'label': 'Terminadas',
                    'data': [{'x': c.name, 'y': c.num_ua} for c in groupby_type('finish')]
                }]
            }
        }

        print([{'x': c.name, 'y': c.num_ua} for c in groupby_type('started')])

    elif chart == 'categories':
        context = {
            'title': 'Categorias de actividades mas realizadas',
            'data': {
                'labels': [c.name for c in groupby_category()],
                'datasets': [{
                    'label': 'Total',
                    'data': [{'x': c.name, 'y': c.num_ua} for c in groupby_category()],
                }, {
                    'label': 'Sin terminar',
                    'data': [{'x': c.name, 'y': c.num_ua} for c in groupby_category('started')],
                }, {
                    'label': 'Terminadas',
                    'data': [{'x': c.name, 'y': c.num_ua} for c in groupby_category('finish')]
                }]
            }
        }

    return JsonResponse(context)
