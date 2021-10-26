from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers import serialize
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return render(request,'grupalActivities/grupalActivities.html')

def myactivity(request):
    return render(request,'grupalActivities/myActivities.html')

@csrf_exempt
def misActividades(request):
  if request.method == 'GET':
    print("my_activities")
    my_activities = groupActivity.objects.filter(User=request.session['_auth_user_id'])
    context = {
      'my_activities': my_activities
    }
    return render(request, context=context)
  return render(request, context={'status':400})

