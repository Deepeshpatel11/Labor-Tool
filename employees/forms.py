from django import forms
from django.core.validators import RegexValidator
from .models import Employee


class EmployeeForm(forms.ModelForm):
    # only digits allowed, at least one character
    gpid = forms.CharField(
        label="GPID",
        validators=[
            RegexValidator(
                regex=r'^\d+$',
                message="GPID must contain only digits.",
                code='invalid_gpid'
            )
        ],
        widget=forms.TextInput(
            attrs={
                'pattern': r'\d+',
                'title': 'Enter digits only',
                'placeholder': 'e.g. 123456'
            }
        )
    )

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
