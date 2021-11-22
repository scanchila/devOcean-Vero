from django.urls import path
from . import views


urlpatterns = [
    path('grupalActivity/<int:activity_id>/',
         views.GrupalActivity_selection, name='grupal_activity_selection'),
    path('grupalActivityIns/<int:activity_id>/',
         views.grupalActivity_inscribir, name='grupalActivity_inscribir'),
    path('grupalActivities/', views.index, name='grupalActivities'),
    path('myActivities/', views.myactivity, name='myActivities'),
    path('filtroActividadesgrupales/', views.grupal, name='filtroActividadesgrupales'),
    path('recibirActividadGrupal/', views.recibirActividadGrupal, name='recibirActividadGrupal')
    
]
