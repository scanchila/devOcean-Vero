import datetime
from django.db import models

class challenges(models.Model):
    days = models.IntegerField(default=0)
    num_audio = models.IntegerField(default=0)
    num_reading = models.IntegerField(default=0)
    num_video = models.IntegerField(default=0)

    def __str__(self):
        return self.name