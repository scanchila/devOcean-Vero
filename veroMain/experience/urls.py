from django.urls import path
from . import views

urlpatterns = [
    path('experience/', views.experience, name='experience')
]
