from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Candidate
from django.urls import reverse
from django.http import HttpResponseForbidden

from .forms import CandidateProfileForm


# Create your views here.

class CandidateSignupView(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    model = User
    template_name = 'candidate_register.html'
    success_message = 'Congratulations, you are registered!'
    success_url = reverse_lazy('candidate:candidate-profile-update')  # Redirect to profile update after sign-up

#Page that show "Update Candidate profile form"
class CandidateProfileView(LoginRequiredMixin, CreateView):
    model = Candidate
    form_class = CandidateProfileForm
    template_name = 'candidate_profile_update.html'
    context_object_name = 'candidate'
    login_url = '/accounts/login/'

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # The user is automatically assigned via LoginRequiredMixin
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return form

    def form_valid(self, form):
        # Proceed with the form validation and saving
        return super().form_valid(form)

    success_url = reverse_lazy('candidate:candidate-home')  # Redirect to home after profile update



class CandidateHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'candidate-home.html'
    login_url = '/accounts/login/'  # Specify the login URL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Ensure this gets the context from the parent
        # Add candidate data to context
        candidate = Candidate.objects.filter(user=self.request.user).first()

        if candidate:
            context['candidate'] = candidate
        else:
            # Optional: You can add an error message or redirect if no Candidate profile is found
            context['error'] = "No candidate profile found for this user."
            context['profile_update_url'] = reverse(
                'candidate:candidate-profile-update')  # Link to the profile update page

        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  # Call the parent class's get_context_data method
    #     # Retrieve the single candidate object for the logged-in user
    #     context['candidate'] = get_object_or_404(Candidate, user=self.request.user)
    #     return context


class CustomLoginView(LoginView):
    template_name = 'custom_login.html'  # Path to your custom login template
    success_url = reverse_lazy('candidate-home')  # Redirect to candidate-home after successful login

