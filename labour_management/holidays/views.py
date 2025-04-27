# holidays/views.py
from datetime import date, timedelta
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages

from employees.models import Employee
from .models import HolidayRequest
from .forms import HolidayRequestForm

class HolidayRotaView(TemplateView):
    template_name = "holidays/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # 1st of this month → 31 days
        start = date.today().replace(day=1)
        dates = [start + timedelta(days=i) for i in range(31)]
        ctx["dates"] = dates

        # all active employees
        emps = Employee.objects.filter(active=True).select_related("area")
        ctx["employees"] = emps

        # build a matrix: { emp.pk: { date: status_string } }
        matrix = {e.pk: {} for e in emps}
        qs = HolidayRequest.objects.filter(
            start_date__lte=dates[-1], end_date__gte=dates[0]
        ).select_related("employee")
        for r in qs:
            for d in dates:
                if r.start_date <= d <= r.end_date:
                    matrix[r.employee_id][d] = r.get_status_display()
        ctx["matrix"] = matrix

        return ctx

class HolidayRequestListView(ListView):
    model               = HolidayRequest
    template_name       = "holidays/requests.html"
    context_object_name = "requests"
    paginate_by         = 20

class HolidayRequestCreateView(CreateView):
    model         = HolidayRequest
    form_class    = HolidayRequestForm
    template_name = "holidays/request_form.html"
    success_url   = reverse_lazy("holidays_index")

def approve_holiday(request, pk):
    hr = get_object_or_404(HolidayRequest, pk=pk)
    hr.status = HolidayRequest.STATUS_APPROVED
    hr.reviewed_at = timezone.now()
    hr.save()
    messages.success(request, f"Holiday for {hr.employee.full_name} approved.")
    return redirect("holidays_index")

def reject_holiday(request, pk):
    hr = get_object_or_404(HolidayRequest, pk=pk)
    hr.status = HolidayRequest.STATUS_REJECTED
    hr.reviewed_at = timezone.now()
    hr.save()
    messages.success(request, f"Holiday for {hr.employee.full_name} rejected.")
    return redirect("holidays_index")
