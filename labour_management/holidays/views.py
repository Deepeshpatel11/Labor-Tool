from django.shortcuts import render, redirect

# Sample employee data (Replace this with actual database records later)
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

        # Simulate saving to the database (Replace with actual model later)
        print(f"Holiday request: {employee_id}, {start_date} to {end_date}, Reason: {reason}")

        return redirect("holidays_index")  # Redirect to holidays home after submission

    return render(request, "holidays/request.html", {"employees": employees})
