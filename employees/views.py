from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# add this import:
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import EmployeeForm
from .models import Employee


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = "employees/index.html"
    context_object_name = "employees"
    # where to redirect if not logged in:
    login_url = reverse_lazy("login")


class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees_index")
    login_url = reverse_lazy("login")


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employees_index")
    login_url = reverse_lazy("login")


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("employees_index")
    login_url = reverse_lazy("login")
