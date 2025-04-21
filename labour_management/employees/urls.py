from django.urls import path
from .views import (
    EmployeeListView,
    EmployeeCreateView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)

urlpatterns = [
    path("", EmployeeListView.as_view(), name="employees_index"),
    path("add/", EmployeeCreateView.as_view(), name="employees_create"),
    path("<int:pk>/edit/", EmployeeUpdateView.as_view(), name="employees_update"),
    path("<int:pk>/delete/", EmployeeDeleteView.as_view(), name="employees_delete"),
]
