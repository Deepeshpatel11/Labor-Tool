from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    """
    Reports homepage – currently under construction.
    Only logged-in users may view this.
    """
    return render(request, "reports/index.html")


@login_required
def labour_report(request, time_filter=None):
    """
    Labour report is not ready yet.
    Only logged-in users may hit this URL.
    """
    raise Http404("Labour report is under construction")
