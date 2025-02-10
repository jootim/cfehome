from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CustomLoginView, CandidateHomeView

urlpatterns = [

    path('',views.CandidateSignupView.as_view(), name='candidate-signup'),
    path('home/', CandidateHomeView.as_view(), name='candidate-home'),
    path('profile-update/',views.CandidateProfileView.as_view(), name='candidate-profile-update'),
    # path('accounts/login/', CustomLoginView.as_view(), name='login'),  # Custom login view

]
