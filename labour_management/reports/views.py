from django.shortcuts import render
from django.http import Http404

def index(request):
    """
    Reports homepage – currently under construction.
    """
    return render(request, "reports/index.html")

def labour_report(request, time_filter=None):
    """
    Labour report is not ready yet.
    """
    raise Http404("Labour report is under construction")
