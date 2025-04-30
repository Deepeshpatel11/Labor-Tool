# labour_management/skills/views.py

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import EmployeeSkill
from .forms import EmployeeSkillForm


class SkillListView(LoginRequiredMixin, ListView):
    """
    Lists all employee skills.  Requires login.
    """
    login_url = reverse_lazy("login")
    model = EmployeeSkill
    template_name = "skills/index.html"
    context_object_name = "skills"


class SkillCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new EmployeeSkill.  Requires login.
    """
    login_url = reverse_lazy("login")
    model = EmployeeSkill
    form_class = EmployeeSkillForm
    template_name = "skills/skill_form.html"
    success_url = reverse_lazy("skills_index")


class SkillUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing EmployeeSkill.  Requires login.
    """
    login_url = reverse_lazy("login")
    model = EmployeeSkill
    form_class = EmployeeSkillForm
    template_name = "skills/skill_form.html"
    success_url = reverse_lazy("skills_index")


class SkillDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete an EmployeeSkill.  Requires login.
    """
    login_url = reverse_lazy("login")
    model = EmployeeSkill
    template_name = "skills/skill_confirm_delete.html"
    success_url = reverse_lazy("skills_index")
