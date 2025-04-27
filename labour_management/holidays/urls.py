# holidays/urls.py
from django.urls import path
from .views import (
    HolidayRotaView,
    HolidayRequestListView,
    HolidayRequestCreateView,
    approve_holiday,
    reject_holiday,
)

urlpatterns = [
    path("", HolidayRotaView.as_view(), name="holidays_index"),
    path("requests/", HolidayRequestListView.as_view(), name="holiday_requests"),
    path("requests/add/", HolidayRequestCreateView.as_view(), name="holiday_request"),
    path("<int:pk>/approve/", approve_holiday, name="holiday_approve"),
    path("<int:pk>/reject/",  reject_holiday,  name="holiday_reject"),
]
