from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Company(models.Model):

    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='company_logo')
    address = models.TextField()
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    email = models.EmailField()
    status = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


