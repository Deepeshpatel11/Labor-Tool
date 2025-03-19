from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="holidays_index"),
    path("request/", views.holiday_request, name="holiday_request"),
    path("approvals/", views.holiday_approvals, name="holiday_approvals"),
    path("approve/<int:request_id>/", views.approve_holiday, name="approve_holiday"),
    path("reject/<int:request_id>/", views.reject_holiday, name="reject_holiday"),
]
