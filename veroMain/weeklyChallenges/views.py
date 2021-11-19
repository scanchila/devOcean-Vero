from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

def weeklyChallenges(request):
    context = {
        'pageTitle': 'Landing'
    }
    return render(request, "weeklyChallenges/weeklyChallenges.html", context)