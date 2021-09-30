from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
  if(request.user.is_authenticated):
    print("esta authenticasdo")
  
  context = {
    'pageTitle' : 'Landing'
  }
  return render(request,"home/landing.html", context)
