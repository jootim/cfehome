from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'homeview'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]