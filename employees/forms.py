from django import forms
from django.contrib.auth import get_user_model
from .models import Employee

User = get_user_model()

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "full_name",
            "gpid",
            "shift",
            "role",
            "line",
            "area",
            "active",
        ]