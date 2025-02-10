from django.forms.models import ModelForm

from .models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'


