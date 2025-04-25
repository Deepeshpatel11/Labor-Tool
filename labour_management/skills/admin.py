from django.contrib import admin
from .models import Area, SkillMaster, EmployeeSkill

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(SkillMaster)
class SkillMasterAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(EmployeeSkill)
class EmployeeSkillAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "primary_skill",
        "show_additional_skills",
    )
    list_filter = ("primary_skill", "employee__shift")
    search_fields = ("employee__full_name", "primary_skill__name")
    raw_id_fields = ("employee", "primary_skill", "additional_skills")

    def show_additional_skills(self, obj):
        return ", ".join(sk.name for sk in obj.additional_skills.all())
    show_additional_skills.short_description = "Additional Skills"
