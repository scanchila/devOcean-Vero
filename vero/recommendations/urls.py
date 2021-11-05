from django.urls import path
from . import views

urlpatterns = [
    path('recommendations/', views.recommendations, name='recommendations'),
    path('filterRecommendations/', views.filterRecommendations, name='filterRecommendations')
]
