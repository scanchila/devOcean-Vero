from django.urls import path
from . import views

urlpatterns = [
    path('personalActivity/<int:activity_id>/',
         views.singleActivity, name='single_activity'),
    path('personalActivity_selection/<int:activity_id>/',
         views.singleActivity_selection, name='single_activity_selection'),
    path('personalActivity_finish/<int:activity_id>/',
         views.singleActivity_finish, name='single_activity_finish'),
    path('', views.main, name='personal_activities_list'),
    path('recibirActividad/', views.recibirActividad, name='recibirActividad'),
]