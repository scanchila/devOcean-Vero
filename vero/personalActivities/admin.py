from django.contrib import admin
from .models import ActivityType, PersonalActivites, ActivityCategory
# Register your models here.

admin.site.register(ActivityType)
admin.site.register(PersonalActivites)
admin.site.register(ActivityCategory)

