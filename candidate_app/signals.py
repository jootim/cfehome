# candidate_app/signals.py


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Candidate

@receiver(post_save, sender=User)
def create_candidate_profile(sender, instance, created, **kwargs):
    if created:
        # Automatically create a Candidate profile when a new User is created
        Candidate.objects.create(user=instance)
