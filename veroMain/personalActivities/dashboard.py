from .models import ActivityType, ActivityCategory, PersonalActivites
from users.models import User_activity
from encuesta.models import Encuesta
from django.db.models import Count


def most_view_activities(status=""):
    if not status:
        return PersonalActivites.objects.annotate(num_ua=Count('user_activity')).order_by('-num_ua')
    else:
        return PersonalActivites.objects.filter(user_activity__status=status).annotate(num_ua=Count('user_activity')).order_by('-num_ua')


def groupby_type(status=""):
    if not status:
        return ActivityType.objects.annotate(num_ua=Count('personalactivites__user_activity')).order_by('name')
    else:
        return ActivityType.objects.filter(personalactivites__user_activity__status=status).annotate(num_ua=Count('personalactivites__user_activity')).order_by('name')


def groupby_category(status=""):
    if not status:
        return ActivityCategory.objects.annotate(num_ua=Count('personalactivites__user_activity')).filter(num_ua__gt=0).order_by('name')
    else:
        return ActivityCategory.objects.filter(personalactivites__user_activity__status=status).annotate(num_ua=Count('personalactivites__user_activity')).order_by('name')
