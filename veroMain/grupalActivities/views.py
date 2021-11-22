from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import eventRegisterForm
from django.contrib.auth.decorators import login_required
from .models import GroupActivity
from django.views.decorators.csrf import csrf_exempt
import datetime
from personalActivities.models import ActivityCategory, PersonalActivites
from .models import GroupActivity
from users.models import User_activity
# Create your views here.


@login_required(login_url='/users/login/')
def index(request):
    context = {
        'pageTitle': 'CreateEvent',
    }
    if request.method == 'POST':
        form = eventRegisterForm(request.POST)
        if form.is_valid():
            groupActivity = GroupActivity(name=form.cleaned_data["nombre"],
                                          address=form.cleaned_data["direccion"],
                                          contact=form.cleaned_data.get(
                                              "email"),
                                          date=form.cleaned_data.get("fecha"),
                                          duration=form.cleaned_data.get(
                                              "duracion"),
                                          hour=form.cleaned_data.get("hora"),
                                          description=form.cleaned_data.get(
                                              "descripcion"),
                                          type_id=form.cleaned_data["tipo"],
                                          creator=request.user
                                          )

            groupActivity.save()
            return redirect('index')

        else:
            print(form.errors)
            context['form'] = form
            return render(request,  'grupalActivities/grupalActivities.html', context)
    else:
        form = eventRegisterForm()
        act_cat = ActivityCategory.objects.all()
        context['act_type'] = act_cat
        context['form'] = form
        return render(request,  'grupalActivities/grupalActivities.html', context)


@csrf_exempt
def myactivity(request):
    if request.method == 'GET':
        print("my_activities")
        my_activities = GroupActivity.objects.filter(creator=request.user)
        context = {
            'my_activities': my_activities
        }
        return render(request, 'grupalActivities/myActivities.html', context=context)
    return render(request, 'grupalActivities/myActivities.html')

@login_required(login_url='/users/login/')
def recibirActividadGrupal(request):
    context = {}
    if request.method == "POST":
        activities = GroupActivity.objects.all()

        if request.POST["time"] != "any":
            args = request.POST["time"].split(",")
            activities = activities.filter(duration__gte=datetime.timedelta(
                minutes=int(args[0])), duration__lte=datetime.timedelta(minutes=int(args[1])))

        if request.POST["act_type"] != "any":
            a_type = request.POST["act_type"]
            print(a_type)
            activities = activities.filter(type_id=a_type)

    act_type = ActivityCategory.objects.all()
    context = {
        "pageTitle": "Grupal Activities list",
        "activities": activities,
        "act_type": act_type
    }

    return render(request, "grupalActivities/filtroActividadesgrupales.html", context)


def grupal(request):
    act_type = ActivityCategory.objects.all()
    activities = GroupActivity.objects.all()
    context = {
        "pageTitle": "Grupal Activities list",
        "activities": activities,
        "act_type": act_type
    }
    return render(request, "grupalActivities/filtroActividadesgrupales.html", context)

@login_required(login_url='/users/login/')
def grupalActivity_selection(request, activity_id):
    activity = GroupActivity.objects.get(id=activity_id)
    user_profile = request.user.user_profile
    try:  # el usuario ya inicio la actividad pero no la ha finalizado
        User_grupal_activity = User_grupal_activity.objects.get(
            user=user_profile, activity=activity, status='started')

    except User_grupal_activity.DoesNotExist as e:
        encuesta = Encuesta(sentimientoInicial="", sentimientoFinal="")
        encuesta.save()
        User_grupal_activity = User_grupal_activity(
            user=user_profile, activity=activity, encuesta=encuesta)
        User_grupal_activity.save()

    return redirect('encuestaAntes', activity_id=User_grupal_activity.id)
'''
@login_required(login_url='/users/login/')
def GrupalActivity_selection(request, activity_id):
    activity = GroupActivity.objects.get(pk=activity_id)
    context = {
        "activity": activity
    }
    return render(request,'grupalActivities/Activity.html', context)
'''