from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

def experience(request):
   
  return render(request,"experience/experience.html")
