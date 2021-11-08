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
def recommendations(request):
    
    return render(request, "recommendations/recommendations.html")

@login_required(login_url='/users/login/')
def filterRecommendations(request):
    
    return render(request, "recommendations/formularioRecomendaciones.html")


@login_required(login_url='/users/login/')
def makeRecommendations(request):
    context = {
        'pageTitle': 'CreateEvent',
    }
    if request.method == 'POST':
        form = None #eventRegisterForm(request.POST) #
        if form.is_valid():
            pass
            #Nombre tipo Género imagen descripcion


    return render(request)