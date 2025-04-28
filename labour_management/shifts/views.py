from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """
    Shows a simple 'Under Construction' splash page.
    Only authenticated users may access this.
    """
    return render(request, 'shifts/index.html')

@login_required
def manning_rota(request, date):
    """
    All rota work is still being rebuilt — 404 for now.
    Only authenticated users may access this.
    """
    raise Http404("Manning Rota is under construction")
