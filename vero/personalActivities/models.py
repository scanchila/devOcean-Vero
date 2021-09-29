import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class ActivityType(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class PersonalActivites(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  imageURL = models.CharField(max_length=255)
  videoURL = models.CharField(max_length=255)
  lecture = models.CharField(max_length=255)
  pub_data = models.DateTimeField('date published')
  duration = models.DurationField(max_length=255)
  activityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)

  def wasPublishedRecently(self):
    return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

  def __str__(self):
    return self.name



