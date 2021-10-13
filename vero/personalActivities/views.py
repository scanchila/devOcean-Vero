from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


from .models import ActivityType, ActivityCategory, PersonalActivites

# Create your views here.
@login_required(login_url='/users/login/')
def main(request):
  all_activities = PersonalActivites.objects.order_by('-pub_data')
  context = {
    "pageTitle": "Personal Activities list",
    "activities": all_activities
  }


  return render(request, "personalActivities/personalActivitiesList.html", context)


@login_required(login_url='/users/login/')
def singleActivity(request, activity_id):
  activity = get_object_or_404(PersonalActivites, pk=activity_id)
  context = {
    "activity" : activity
  }
  return render(request, "personalActivities/activity.html", context)
