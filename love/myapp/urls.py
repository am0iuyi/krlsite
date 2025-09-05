from django.urls import path
from . import views

# Уберите app_name если не используете пространства имен
urlpatterns = [
    path('', views.home, name='home'),
    path('game/', views.game, name='game'),
    path('facts/', views.facts, name='facts'),
    path('thoto/', views.thoto, name='thoto'),
    path('history/', views.history, name='history'),
    path('love/', views.love, name='love'),
]