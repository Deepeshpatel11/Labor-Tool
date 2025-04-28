from django.shortcuts import render
from django.http import Http404

def index(request):
    """
    Shows a simple 'Under Construction' splash page.
    """
    return render(request, 'shifts/index.html')

def manning_rota(request, date):
    """
    All rota work is still being rebuilt — 404 for now.
    """
    raise Http404("Manning Rota is under construction")
