from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json
from weeklyChallenges.models import Challenges

def weeklyChallenges(request):


    try:
        ans = Challenges.objects.get(user=request.user)
        print(ans)
    except:
            ans = Challenges(user=request.user, days=1)
            ans.save()

    context = {
        'pageTitle': 'Desafios Semanales',
        'challenge': ans,
        'proDays': int((ans.days / 7) * 100),
        'proRead': int((ans.num_reading / 7) * 100),
        'proAudio': int((ans.num_audio / 7) * 100),
        'proVideo': int((ans.num_video / 7) * 100)
    }
    return render(request, "weeklyChallenges/weeklyChallenges.html", context)