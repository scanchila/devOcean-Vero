from personalActivities.models import ActivityType, ActivityCategory, PersonalActivites
import datetime


activities = ActivityType.objects.all()

if(category != "any"):
    activities = activities.filter(categorty_id=cat_id)

if("type" != any):
    activities = activities.filter(activityType_id=act_ty_id)
