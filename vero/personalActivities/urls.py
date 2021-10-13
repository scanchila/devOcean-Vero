from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='personalActivities'),
    path('', views.main, name='personal_activities_list'),
]
