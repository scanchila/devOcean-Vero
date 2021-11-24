from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import eventRegisterForm
from django.contrib.auth.decorators import login_required
from .models import GroupActivity
from django.views.decorators.csrf import csrf_exempt
import datetime
from personalActivities.models import ActivityCategory
from grupalActivities.models import GroupActivity
import random
import time
#import sklearn.metrics.pairwise
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


def recommendation(request):
    user = request.user
    MIN_TIME = request.GET.get('MINTIME',300)
    ALL_RECOMMEND = request.GET.get('ALLRECOMMEND',10)
    #POPULAR_RECOMMEND = 5
    TYPE_RECOMMEND = request.GET.get('TYPE_RECOMMEND',5)
    TYPE_AMOUNT = request.GET.get('TYPE_AMOUNT',3)
    data = user.user_profile.completed_group_activities.all()
    all_types = {x.type:i for i,x in enumerate(GroupActivity.objects.all())}
    activities = GroupActivity.objects.all().difference(data)
    filtr = lambda x, MIN_TIME: (((int(time.mktime(x.date.timetuple())))+MIN_TIME)>time.time()
                                 
                                 )
    x = [[ob,all_types[ob.type], ob.duration, int(time.mktime(ob.date.timetuple()))] for ob in data]
    foo = lambda x: x[1]
    most_types = [ob.type for ob in data]
    most_types = [(ob,  most_types.count(ob)) for ob in set(most_types)][:]

    y = [(ob, all_types[ob.type], ob.duration, int(time.mktime(ob.date.timetuple())), len(ob.user_profile_set.all())) for ob in activities if filtr(ob,MIN_TIME)]
    foo = lambda x: x[3] #completion quantity
    y.sort(key=foo)
    y =  y[:ALL_RECOMMEND]
    y = set(y+[(ob, all_types[ob.type], ob.duration, int(time.mktime(ob.date.timetuple())), len(ob.user_profile_set.all())) for ob in activities if ob.type in most_types])
    
    print(GroupActivity.objects.all())
    context = {'recommendations':y}
    return render(request, "grupalActivities/filtroActividadesgrupales.html", context)

