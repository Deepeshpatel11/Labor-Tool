# labour_management/admin.py
from django.contrib import admin
from .models import Employee, Skill, HolidayRequest, Shift, ManningAssignment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display  = ('user', 'gpid', 'shift', 'role', 'area', 'active')
    search_fields = ('user__username', 'gpid', 'role', 'area')
    list_filter   = ('shift', 'area', 'active')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ('employee', 'name')
    search_fields = ('employee__user__username', 'name')

@admin.register(HolidayRequest)
class HolidayRequestAdmin(admin.ModelAdmin):
    list_display  = ('employee', 'start_date', 'end_date', 'status')
    list_filter   = ('status',)
    date_hierarchy = 'start_date'

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display  = ('date', 'shift_type', 'scenario1', 'scenario2', 'scenario3', 'scenario4')
    list_filter   = ('shift_type', 'date')
    date_hierarchy = 'date'

@admin.register(ManningAssignment)
class ManningAssignmentAdmin(admin.ModelAdmin):
    list_display  = ('shift', 'line_number', 'scenario', 'sub_area', 'role', 'employee', 'hours')
    list_filter   = ('line_number', 'scenario', 'shift__date')
    raw_id_fields = ('employee',)
