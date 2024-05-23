from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='stage-index'),
    path('about/', views.about, name='stage-about')
]