from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="holidays_index"),
    path("request/", views.holiday_request, name="holiday_request"),
]
