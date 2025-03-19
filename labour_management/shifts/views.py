from django.shortcuts import render

# Sample shift data
shifts_data = [
    {"date": "2025-03-20", "shift_type": "Day", "staffing": "Normal"},
    {"date": "2025-03-20", "shift_type": "Night", "staffing": "Understaffed"},
    {"date": "2025-03-21", "shift_type": "Day", "staffing": "Normal"},
    {"date": "2025-03-21", "shift_type": "Night", "staffing": "Full"},
]

# Sample manning rota data
rota_data = {
    "2025-03-20_Day": [
        {"name": "John Smith", "role": "Supervisor", "area": "Process"},
        {"name": "Alice Johnson", "role": "Technician", "area": "Packaging"},
    ],
    "2025-03-20_Night": [
        {"name": "David Brown", "role": "Operator", "area": "Multipack"},
        {"name": "Sarah Lee", "role": "Technician", "area": "Palletising"},
    ],
}

def index(request):
    return render(request, "shifts/index.html", {"shifts": shifts_data})

def manning_rota(request, date, shift_type):
    rota_key = f"{date}_{shift_type}"
    rota = rota_data.get(rota_key, [])  # Get rota for the specific date/shift, or empty list if not found
    return render(request, "shifts/manning_rota.html", {"date": date, "shift_type": shift_type, "rota": rota})
