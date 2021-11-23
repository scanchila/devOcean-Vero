import datetime
from django.db import models
from django.contrib.auth.models import User


class Challenges(models.Model):
    name = models.CharField(max_length=255, default="")
    days = models.IntegerField(default=0)
    num_audio = models.IntegerField(default=0)
    num_reading = models.IntegerField(default=0)
    num_video = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name