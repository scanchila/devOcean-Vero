from django.urls import path
from . import views


urlpatterns = [
    path('grupalActivities/', views.index, name='grupalActivities'),
]
