from django.contrib import admin
from .models import Area, Skill

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display  = ("name",)
    search_fields = ("name",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display   = ("employee", "name")
    list_filter    = ("name",)
    search_fields  = ("employee__full_name", "name")
    autocomplete_fields = ("employee",)