from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'portblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('archive/', views.archive, name='archive'),
]
