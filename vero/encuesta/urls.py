from django.urls import path
from . import views

urlpatterns = [
    path('encuesta/', views.encuestaDespues, name='encuesta'),
    path('encuestaAntes/<int:activity_id>/', views.index, name='encuestaAntes'),
    path('recibirEncuesta/', views.recibirEncuesta, name='recibirEncuesta')
]
