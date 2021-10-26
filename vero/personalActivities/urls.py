from django.urls import path
from . import views

urlpatterns = [
    path('personalActivity/<int:activity_id>/<feeling>',
         views.singleActivity, name='single_activity'),
    path('personalActivity/<int:activity_id>/',
         views.singleActivity, name='single_activity'),
    path('', views.main, name='personal_activities_list'),
    path('recibirActividad/', views.recibirActividad, name='recibirActividad')
]
