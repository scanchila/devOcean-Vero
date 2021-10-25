from personalActivities.models import ActivityType, ActivityCategory, PersonalActivites
import datetime

ActivityType.objects.all()


v = ActivityType.objects.get(name="Video")  # actividad tipo  - video
videos = v.personalactivites_set.all()  # actividades que son videos
videos.filter(duration__gte=datetime.timedelta(minutes=5), duration__lte=datetime.timedelta(
    minutes=10))  # video que duran entre 5 a 10 minutos
