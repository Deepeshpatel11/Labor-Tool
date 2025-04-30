from django.contrib import admin
from .models import HolidayRequest


@admin.register(HolidayRequest)
class HolidayRequestAdmin(admin.ModelAdmin):
    list_display = (
        "employee",
        "start_date",
        "end_date",
        "status",
        "requested_at",
        "reviewed_at",
    )
    list_filter = ("status", "start_date", "employee__shift", "employee__area")
    search_fields = ("employee__full_name", "employee__gpid")
    date_hierarchy = "start_date"
