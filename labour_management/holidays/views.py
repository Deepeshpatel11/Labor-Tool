from django.shortcuts import render, redirect

# Sample holiday request data (Replace this with actual database logic later)
holiday_requests = [
    {"id": 1, "employee": "John Smith", "start_date": "2025-04-01", "end_date": "2025-04-05", "status": "Pending"},
    {"id": 2, "employee": "Alice Johnson", "start_date": "2025-04-10", "end_date": "2025-04-12", "status": "Pending"},
]

employees = [
    {"id": 1, "name": "John Smith"},
    {"id": 2, "name": "Alice Johnson"},
]

def index(request):
    return render(request, "holidays/index.html")

def holiday_request(request):
    if request.method == "POST":
        employee_id = request.POST.get("employee")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        reason = request.POST.get("reason")

        # Simulate saving to the database
        print(f"Holiday request: {employee_id}, {start_date} to {end_date}, Reason: {reason}")

        return redirect("holidays_index")

    return render(request, "holidays/request.html", {"employees": employees})

def holiday_approvals(request):
    return render(request, "holidays/approvals.html", {"holiday_requests": holiday_requests})

def approve_holiday(request, request_id):
    for req in holiday_requests:
        if req["id"] == request_id:
            req["status"] = "Approved"
    return redirect("holiday_approvals")

def reject_holiday(request, request_id):
    for req in holiday_requests:
        if req["id"] == request_id:
            req["status"] = "Rejected"
    return redirect("holiday_approvals")
