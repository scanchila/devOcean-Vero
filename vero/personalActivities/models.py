import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class ActivityType(models.Model):
  name = models.CharField(max_length=254, unique=True)
  description = models.CharField(max_length=254)

  def __str__(self):
    return self.name


class ActivityCategory(models.Model):
  name = models.CharField(max_length=254, unique=True)
  description = models.CharField(max_length=254)

  def __str__(self) -> str:
    return self.name

class PersonalActivites(models.Model):
  name = models.CharField(max_length=254, unique=True)
  description = models.CharField(max_length=254)
  image_URL = models.URLField(max_length=1000, blank=True)
  video_URL = models.URLField(max_length=1000, blank=True)
  lecture = models.CharField(max_length=1000000, blank=True)
  pub_data = models.DateTimeField('date published')
  duration = models.DurationField()
  activityType = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
  categories = models.ManyToManyField(ActivityCategory)

  def wasPublishedRecently(self):
    return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

  def __str__(self):
    return self.name



