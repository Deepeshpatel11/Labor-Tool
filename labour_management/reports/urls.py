from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="reports_index"),
    path("labour-analysis/", views.labour_report, name="labour_report"),
]
