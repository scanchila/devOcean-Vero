from django.db import models
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class GroupActivity(models.Model):
  name = models.CharField(max_length=255, unique=True)
  description = models.CharField(max_length=254)
  type = models.CharField(max_length=254)
  duration = models.CharField(max_length=255)
  date = models.DateTimeField()
  hour = models.CharField(max_length=255)
  address =  models.CharField(max_length=254)
  contact = models.CharField(max_length=254)
  creator = models.OneToOneField(User, on_delete=models.CASCADE)


