from django.urls import path
from . import views

urlpatterns = [
    path('encuesta/', views.encuestaDespues, name='encuesta'),
    path('encuestaAntes/', views.index, name='encuestaAntes')
]
