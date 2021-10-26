from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import eventRegisterForm
from django.contrib.auth.decorators import login_required
from .models import GroupActivity
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@login_required(login_url='/users/login/')
def index(request):
    context = {
        'pageTitle' : 'CreateEvent',
    }
    if request.method == 'POST':
        form = eventRegisterForm(request.POST)
        if form.is_valid():
            groupActivity = GroupActivity(name = form.cleaned_data["nombre"],       
                                          address = form.cleaned_data["direccion"],
                                          contact = form.cleaned_data.get("email"),
                                          date = form.cleaned_data.get("fecha"),
                                          duration = form.cleaned_data.get("duracion"),
                                          hour = form.cleaned_data.get("hora"),
                                          description = form.cleaned_data.get("descripcion"),
                                          type = form.cleaned_data["tipo"],
                                          creator = request.user
                                          )
          
            groupActivity.save()
            return redirect('index')
            
        else:
            print(form.errors)
            context['form'] = form
            return render(request,  'grupalActivities/grupalActivities.html', context)
    else:
        form = eventRegisterForm()
        context['form'] = form
        return render(request,  'grupalActivities/grupalActivities.html', context)

@csrf_exempt
def myactivity(request):
  if request.method == 'GET':
    print("my_activities")
    my_activities = GroupActivity.objects.filter(creator=request.user)
    context = {
      'my_activities': my_activities
    }
    return render(request, 'grupalActivities/myActivities.html', context=context)
  return render(request, 'grupalActivities/myActivities.html')