from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models



class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    def __str__(self):
        return self.user.username

