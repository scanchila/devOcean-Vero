import datetime

from django.db import models
from django.utils import timezone

class Recommendations(models.Model):
    name = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    description = models.CharField(max_length=700)
    gender = models.CharField(max_length=254)

    def __str__(self) -> str:
        return self.name