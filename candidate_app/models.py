import datetime

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Candidate(models.Model):

    gender = {
        'male': 'Male',
        'female': 'Female',
        'LGBTQ' : 'LGBTQ',
    }
    payment_preference = {
        'cash': 'Cash',
        'monthly': 'Monthly',
        'ok to all': 'Ok to All',

    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    year_of_birth = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1974), max_value_current_year])
    gender = models.CharField(max_length=6, choices=gender.items(),default='male')
    payment_preference = models.CharField(max_length=9, choices=payment_preference.items(),default='cash')
    availabilities = models.TextField(blank=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
