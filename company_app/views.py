from importlib.metadata import requires

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView, DetailView

from .forms import CompanyForm
from .models import Company, Employee


# Create your views here.

class CompanyHomeView( LoginRequiredMixin,ListView ):
    model = Employee
    context_object_name = 'employee'




class CompanyProfileCreate(CreateView):
    form_class = CompanyForm
    model = Company
    success_url = 'company-home'


