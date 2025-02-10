# candidate_app/apps.py

from django.apps import AppConfig

class CandidateAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'candidate_app'

    def ready(self):
        import candidate_app.signals  # Ensure signals are registered
