from django.shortcuts import render

# Sample placeholder data
skills_data = [
    {"name": "John Smith", "shift": "Red", "role": "Technician", "primary_skill": "Electrical", "secondary_skill": "Fryer Operator", "tertiary_skill": None},
    {"name": "Alice Johnson", "shift": "Green", "role": "Manufacturing Technician", "primary_skill": "Packaging", "secondary_skill": "Primary Operator", "tertiary_skill": None},
    {"name": "David Brown", "shift": "Blue", "role": "General Operator", "primary_skill": "Packing", "secondary_skill": None, "tertiary_skill": None},
]

def index(request):
    return render(request, "skills/index.html", {"skills": skills_data})
