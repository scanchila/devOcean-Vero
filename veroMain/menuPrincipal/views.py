from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
  if(request.user.is_authenticated):
    return redirect("home")
  
  context = {
    'pageTitle' : 'Menu principal'
  }
  return render(request,"menuPrincipal/menu.html", context)