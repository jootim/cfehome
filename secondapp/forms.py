from django.forms.models import ModelForm

from .models import Reviews


class SecondForm(ModelForm):
    class Meta:
        model= Reviews
        fields= ['review','rating']