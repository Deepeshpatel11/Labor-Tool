from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display   = ("full_name", "gpid", "shift", "line", "area", "active")
    list_filter    = ("shift", "line", "area", "active")
    search_fields  = ("full_name", "gpid")
    ordering       = ("full_name",)
