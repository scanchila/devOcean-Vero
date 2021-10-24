from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


from personalActivities.models import PersonalActivites

# Create your models here.


class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.IntegerField(default=0)
    activities = models.ManyToManyField(
        PersonalActivites, through='User_activity')

    def __str__(self):
        return self.user.username


class User_activity(models.Model):
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    activity = models.ForeignKey(PersonalActivites, on_delete=models.CASCADE)
    date_start = models.DateTimeField('date start', default=timezone.now)
    date_finish = models.DateTimeField('date finish', null=True, blank=True)
    status = models.CharField(max_length=50, default="started")

    class Meta:
        verbose_name = ("User_activity")
        verbose_name_plural = ("User_activitys")

    def __str__(self):
        return self.user.user.username + "_" + self.activity.name

    def get_absolute_url(self):
        return reverse("User_activity_detail", kwargs={"pk": self.pk})
