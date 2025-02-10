from django.forms import forms
from django.forms.models import ModelForm
from django import forms
from .models import Candidate


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name','last_name','email','telephone','year_of_birth','gender','payment_preference']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            # Set the 'user' field to hidden
            self.fields['user'].widget = forms.HiddenInput()

