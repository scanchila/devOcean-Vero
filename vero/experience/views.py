from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json



@login_required(login_url='/users/login/')
def experience(request):


    if request.method == 'GET':
        print("user_info")
        usuario = User.objects.get(id=request.user.id)
        usuario_perfil = usuario.user_profile
        f = open("experience/niveles.json")
        niveles = json.load(f)
        f.close()
        level=0

        for i in range(len(niveles.get("ranges")))[::-1]:
            if usuario_perfil.experience>=float(niveles.get("ranges")[i]):

                level = niveles.get("niveles")[niveles.get('ranges')[i]]
                if i>=len(niveles.get("ranges"))-1:
                    porc = 0
                else:
                    porc = (usuario_perfil.experience-float(niveles.get("ranges")[i]))/float(niveles.get("ranges")[i+1])
                break


        context = {
          'user_info': usuario_perfil,
          'level':level,
          'porc':round(porc*100,2),
          'anim': 1440-1440*porc
        }
        return render(request, 'experience/experience.html' ,context=context)
    return render(request, 'experience/experience.html' ,context={'status':400})