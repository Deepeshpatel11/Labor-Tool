from django.shortcuts import render
from datetime import date

# Sample labour data (Replace with actual database queries later)
labour_data = [
    {"name": "John Smith", "role": "Technician", "hours": 40, "hourly_rate": 20},
    {"name": "Alice Johnson", "role": "Supervisor", "hours": 45, "hourly_rate": 25},
    {"name": "David Brown", "role": "Operator", "hours": 38, "hourly_rate": 18},
    {"name": "Sarah Lee", "role": "Technician", "hours": 42, "hourly_rate": 20},
]

# Precompute total cost per employee
for emp in labour_data:
    emp["total_cost"] = emp["hours"] * emp["hourly_rate"]

def index(request):
    return render(request, "reports/index.html")

def labour_report(request):
    total_hours = sum(emp["hours"] for emp in labour_data)
    total_cost = sum(emp["total_cost"] for emp in labour_data)

    return render(request, "reports/labour_report.html", {
        "labour_data": labour_data,
        "total_hours": total_hours,
        "total_cost": total_cost,
        "report_date": date.today()
    })
