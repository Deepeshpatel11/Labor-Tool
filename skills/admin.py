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
        "secondary_skill",
        "tertiary_skill",
    )
    list_filter = (
        "primary_skill",
        "secondary_skill",
        "tertiary_skill",
        "employee__shift",
        "employee__line",
        "employee__area",
    )
    search_fields = (
        "employee__full_name",
        "primary_skill__name",
        "secondary_skill__name",
        "tertiary_skill__name",
    )
    raw_id_fields = ("employee", "primary_skill", "secondary_skill", "tertiary_skill")
