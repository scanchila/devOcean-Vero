from django.urls import path
from . import views

urlpatterns = [
    path('encuesta/<int:activity_id>/', views.encuestaDespues, name='encuesta'),
    path('encuestaAntes/<int:activity_id>/',
         views.index, name='encuestaAntes'),
    path('answerEncuesta/<int:activity_id>/<feeling>/<int:before>',
         views.answerEncuesta, name='recibirEncuesta')
]
