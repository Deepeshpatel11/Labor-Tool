from django import forms
from .models import HolidayRequest

class HolidayRequestForm(forms.ModelForm):
    class Meta:
        model  = HolidayRequest
        fields = ["employee", "start_date", "end_date", "status"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date":   forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # show employee by full name
        self.fields["employee"].label_from_instance = lambda emp: emp.full_name
