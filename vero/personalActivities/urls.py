from django.urls import path
from . import views

urlpatterns = [
    path('listaActividades/', views.main, name='listaActividades'),
    path('actividad/', views.actividad, name='actividad')
]
