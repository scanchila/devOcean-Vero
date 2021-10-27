from django.shortcuts import render, redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.models import User
from encuesta.models import Encuesta
from users.models import User_activity, User_profile
from personalActivities.models import PersonalActivites

# Create your views here.


@login_required(login_url='/users/login/')
def index(request, activity_id):
    context = {
        'activity_id': activity_id,
        'before': 1
    }
    return render(request, "encuesta/encuesta.html", context)


@login_required(login_url='/users/login/')
def encuestaDespues(request, activity_id):
    context = {
        'activity_id': activity_id,
        'before': 0
    }
    return render(request, "encuesta/encuesta.html", context)


@login_required(login_url='/users/login/')
def answerEncuesta(request, activity_id, feeling="", before=0):
    user_activity = User_activity.objects.get(pk=activity_id)
    encuesta = user_activity.encuesta
    aux_experience = 0
    if before:
        print("se recibe la respuesta de la encuesta antes")
        encuesta.sentimientoInicial = feeling
        r = redirect('single_activity', activity_id=activity_id)
    else:
        print("se recibe la respuesta de la encuesta despues")
        encuesta.sentimientoFinal = feeling
        r = redirect('menu')
        aux_experience = 1

    encuesta.save()

    if aux_experience:
        user_profile = request.user.user_profile
        print(user_profile.experience)
        personalActivy = user_activity.activity
        user_profile.experience += int(personalActivy.experience)
        print(user_profile.experience)

        user_profile.save()

    return r
