from django.db import models

# Create your models here.
class Achievement(models.Model):

    experience = models.IntegerField(default=0)
    description = models.CharField(max_length=400, default="NA")
    category = models.CharField(max_length=50, default="NA")
    condition = models.CharField(max_length=50, default="achievement_user_create_account")
