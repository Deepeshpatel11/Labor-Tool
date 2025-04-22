from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

app_name = "employees"

urlpatterns = [
    path("",              EmployeeListView.as_view(),   name="index"),
    path("add/",          EmployeeCreateView.as_view(), name="create"),
    path("<int:pk>/edit/",   EmployeeUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", EmployeeDeleteView.as_view(), name="delete"),
]
