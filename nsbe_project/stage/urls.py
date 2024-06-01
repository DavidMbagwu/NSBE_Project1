from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='stage-index'),
    path('about/', views.about, name='stage-about'),
    path('directory/', views.directory, name='stage-directory'),
    path('events/', views.events, name='stage-events'),
    path('help/', views.help, name='stage-help'),
    path('points/', views.points, name='stage-points'),
    path('profile/', views.profile, name='stage-profile'),
    path('login/', views.login, name='stage-login')
]