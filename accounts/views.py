from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


class CustomLoginView(LoginView):
    template_name = 'custom_login.html'  # Point to your custom template

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('homeview:home')

    def get_next_page(self):
        print("Redirecting to:", self.next_page)  # Check where it's redirecting
        return super().get_next_page()

    @method_decorator(never_cache)  # Add this decorator to avoid caching
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
