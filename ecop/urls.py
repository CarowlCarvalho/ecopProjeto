from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('locais/', views.locais),
    path('localizacao/', views.localizacao),
    path('saibamais/', views.saibamais),
]
