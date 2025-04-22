from django import forms
from django.contrib.auth import get_user_model
from .models import Employee

User = get_user_model()

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "user",
            "gpid",
            "shift",
            "line",
            "area",
            "active",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Order the user dropdown by first+last name
        self.fields["user"].queryset = User.objects.order_by("first_name", "last_name")
        self.fields["user"].label_from_instance = (
            lambda obj: obj.get_full_name() or obj.username
        )
