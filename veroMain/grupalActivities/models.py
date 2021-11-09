from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from personalActivities.models import ActivityCategory

# Create your models here.


class GroupActivity(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=254)
    type = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    duration = models.CharField(max_length=255)
    date = models.DateTimeField()
    hour = models.CharField(max_length=255)
    address = models.CharField(max_length=254)
    contact = models.CharField(max_length=254)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
