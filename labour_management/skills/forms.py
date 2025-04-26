from django import forms
from .models import EmployeeSkill, SkillMaster

class EmployeeSkillForm(forms.ModelForm):
    class Meta:
        model = EmployeeSkill
        fields = ["employee", "primary_skill", "secondary_skill", "tertiary_skill"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # show employee by full_name
        self.fields["employee"].label_from_instance = lambda obj: obj.full_name
        # order all skill dropdowns alphabetically, and include empty label
        qs = SkillMaster.objects.order_by("name")
        for fld in ("primary_skill","secondary_skill","tertiary_skill"):
            f = self.fields[fld]
            f.queryset   = qs
            f.empty_label = "— select —"
