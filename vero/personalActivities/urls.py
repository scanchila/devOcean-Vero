from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='personalActivities'),
    path('personalActivity/<int:activity_id>/', views.singleActivity, name='single_activity'),
    path('', views.main, name='personal_activities_list'),
]
