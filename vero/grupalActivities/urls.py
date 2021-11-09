from django.urls import path
from . import views


urlpatterns = [
    path('grupalActivities/', views.index, name='grupalActivities'),
    path('myActivities/', views.myactivity, name='myActivities'),
    path('filtroActividadesgrupales/', views.grupal, name='filtroActividadesgrupales'),
    path('recibirActividadGrupal/', views.recibirActividadGrupal, name='recibirActividadGrupal'),
    path('grupalActivity_selection/<int:activity_id>/',
         views.grupalActivity_selection, name='grupal_activity_selection')
]
