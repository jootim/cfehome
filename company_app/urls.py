from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import CompanyHomeView, CompanyProfileCreate

urlpatterns = [
    path('company-home',CompanyHomeView.as_view(), name='company-home' ),
    path('create-company/',CompanyProfileCreate.as_view(), name='create-company' ),


    ]

