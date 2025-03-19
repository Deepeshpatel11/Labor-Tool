from django.shortcuts import render
from datetime import date, timedelta

# Sample labour data (Replace with actual database queries later)
labour_data = [
    {"name": "John Smith", "role": "Technician", "hours": 40, "hourly_rate": 20, "date": date(2025, 3, 10)},
    {"name": "Alice Johnson", "role": "Supervisor", "hours": 45, "hourly_rate": 25, "date": date(2025, 3, 5)},
    {"name": "David Brown", "role": "Operator", "hours": 38, "hourly_rate": 18, "date": date(2025, 2, 25)},
    {"name": "Sarah Lee", "role": "Technician", "hours": 42, "hourly_rate": 20, "date": date(2025, 1, 15)},
]

# Precompute total cost per employee
for emp in labour_data:
    emp["total_cost"] = emp["hours"] * emp["hourly_rate"]

def index(request):
    return render(request, "reports/index.html")

def labour_report(request, time_filter=None):
    today = date.today()

    # Apply filtering based on time period
    if time_filter == "weekly":
        start_date = today - timedelta(days=7)
        filtered_data = [emp for emp in labour_data if emp["date"] >= start_date]
    elif time_filter == "monthly":
        start_date = today - timedelta(days=30)
        filtered_data = [emp for emp in labour_data if emp["date"] >= start_date]
    elif time_filter == "yearly":
        start_date = today - timedelta(days=365)
        filtered_data = [emp for emp in labour_data if emp["date"] >= start_date]
    else:
        filtered_data = labour_data  # Show all data if no filter is applied

    total_hours = sum(emp["hours"] for emp in filtered_data)
    total_cost = sum(emp["total_cost"] for emp in filtered_data)

    return render(request, "reports/labour_report.html", {
        "labour_data": filtered_data,
        "total_hours": total_hours,
        "total_cost": total_cost,
        "report_date": today,
        "time_filter": time_filter,
    })
