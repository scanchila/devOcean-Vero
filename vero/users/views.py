from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render

from .forms import UserLoginForm, UserRegisterForm

# Create your views here.


def registerUser(request):
    context = {
        'pageTitle' : 'Register',
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
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')

    else:
        form = UserLoginForm()

    context = {
        'pageTitle' : 'Login',
        'form': form
    }

    return render(request,  'users/login.html', context)

def logoutUser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')
