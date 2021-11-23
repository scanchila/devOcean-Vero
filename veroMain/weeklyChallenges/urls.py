from django.urls import path
from . import views

urlpatterns = [
    path('weeklyChallenges/', views.weeklyChallenges, name='weeklyChallenges'),
]
