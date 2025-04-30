from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomeView(LoginRequiredMixin, TemplateView):
    """
    Landing page shown after login, and at "/"
    """
    template_name = "labour_management/home.html"
