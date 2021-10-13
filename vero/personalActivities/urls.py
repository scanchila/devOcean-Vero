from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='personalActivities'),
    path('personalActivity/<int:activity_id>/', views.singleActivity, name='single_activity'),
    path('', views.temp, name='personal_activities_list'),
    path('listaActividades/', views.main, name='listaActividades'),
    path('actividad/', views.actividad, name='actividad'),
    path('recibirActividad/', views.recibirActividad, name='recibirActividad')
]
