from django.shortcuts import render

# Sample shift data
shifts_data = [
    {"date": "2025-03-20", "shift_type": "Day", "staffing": "Normal"},
    {"date": "2025-03-20", "shift_type": "Night", "staffing": "Understaffed"},
    {"date": "2025-03-21", "shift_type": "Day", "staffing": "Normal"},
    {"date": "2025-03-21", "shift_type": "Night", "staffing": "Full"},
]

def index(request):
    return render(request, "shifts/index.html", {"shifts": shifts_data})
