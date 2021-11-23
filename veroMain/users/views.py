from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.template import RequestContext
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.serializers import serialize
from django.contrib.auth.models import User
from weeklyChallenges.models import Challenges
from datetime import datetime

# Create your views here.


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('personal_activities_list')
    context = {
        'pageTitle': 'Register',
    }
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserRegisterForm()

    context['form'] = form
    return render(request,  'users/register.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        ### Weekly Challenge
        hoy = str(datetime.now().day)
        try:
            ans = Challenges.objects.get(user=request.user)
            ans.name += " " + hoy
            ans.name = set(ans.name.split())
            ans.days = len(ans.name)
            ans.name = " ".join(list(ans.name))
            ans.save()
        except:
            ans = Challenges(user=request.user, days=1,name=hoy)
            ans.save()

        ###
        return redirect('personal_activities_list')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    else:
        form = UserLoginForm()

    context = {
        'pageTitle': 'Login',
        'form': form
    }

    return render(request,  'users/login.html', context)


def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')


@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('index')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }

    return render(request, 'users/update.html', context)

