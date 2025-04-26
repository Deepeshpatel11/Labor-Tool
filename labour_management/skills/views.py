from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import EmployeeSkill
from .forms import EmployeeSkillForm

class SkillListView(ListView):
    model               = EmployeeSkill
    template_name       = "skills/index.html"
    context_object_name = "skills"

class SkillCreateView(CreateView):
    model         = EmployeeSkill
    form_class    = EmployeeSkillForm
    template_name = "skills/skill_form.html"
    success_url   = reverse_lazy("skills_index")

class SkillUpdateView(UpdateView):
    model         = EmployeeSkill
    form_class    = EmployeeSkillForm
    template_name = "skills/skill_form.html"
    success_url   = reverse_lazy("skills_index")

class SkillDeleteView(DeleteView):
    model         = EmployeeSkill
    template_name = "skills/skill_confirm_delete.html"
    success_url   = reverse_lazy("skills_index")
