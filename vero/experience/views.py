from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

def experience(request):
  if request.method == 'GET':
    print("user_info")
    usuario = User.objects.get(id=request.user.id)
    usuario_perfil = usuario.user_profile
    context = {
      'user_info': usuario_perfil
    }
    return render(request, 'experience/experience.html' ,context=context)
  return render(request, 'experience/experience.html' ,context={'status':400})