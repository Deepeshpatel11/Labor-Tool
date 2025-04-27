from datetime import date, timedelta
from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q

from employees.models import Employee
from .models import HolidayRequest
from .forms import HolidayRequestForm


class HolidayRotaView(TemplateView):
    template_name = "holidays/index.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # --- DATES: from Jan 1st to Dec 31st of this year ---
        today = date.today()
        start = today.replace(month=1, day=1)
        end = today.replace(month=12, day=31)
        total_days = (end - start).days + 1
        dates = [start + timedelta(days=i) for i in range(total_days)]
        ctx["dates"] = dates

        # --- BASE EMPLOYEE QS (only active) ---
        emps = Employee.objects.filter(active=True).select_related("area")

        # --- APPLY GET-PARAM FILTERS ---
        q = self.request.GET.get("q", "").strip()
        shift = self.request.GET.get("shift", "")
        area = self.request.GET.get("area", "")
        role = self.request.GET.get("role", "")

        if q:
            emps = emps.filter(
                Q(full_name__icontains=q) |
                Q(gpid__icontains=q)
            )
        if shift:
            emps = emps.filter(shift=shift)
        if area:
            emps = emps.filter(area__name=area)
        if role:
            emps = emps.filter(role=role)

        # --- ORDER: shift → area → role → name ---
        emps = emps.order_by("shift", "area__name", "role", "full_name")
        ctx["employees"] = emps

        # --- LISTS FOR DROPDOWNS ---
        base = Employee.objects.filter(active=True)
        ctx["shifts"] = base.values_list("shift", flat=True).distinct()
        ctx["areas"] = base.values_list("area__name", flat=True).distinct()
        ctx["roles"] = base.values_list("role", flat=True).distinct()

        # --- ONLY VISIBLE EMPLOYEES ---
        employee_ids = [e.pk for e in emps]

        # --- BUILD HOLIDAY STATUS MATRIX ---
        matrix = {pk: {} for pk in employee_ids}
        qs = HolidayRequest.objects.filter(
            start_date__lte=end,
            end_date__gte=start,
            employee_id__in=employee_ids
        ).select_related("employee")
        for r in qs:
            for d in dates:
                if r.start_date <= d <= r.end_date:
                    matrix[r.employee_id][d] = r.get_status_display()
        ctx["matrix"] = matrix

        # --- PRESERVE FILTER VALUES FOR “STICKY” FORM ---
        ctx["filter_q"] = q
        ctx["filter_shift"] = shift
        ctx["filter_area"] = area
        ctx["filter_role"] = role

        # --- PASS DISPLAY-STRING STATUSES INTO TEMPLATE ---
        ctx["approved_statuses"] = (
            HolidayRequest.STATUS_APPROVED,
        )

        return ctx


class HolidayRequestListView(ListView):
    model = HolidayRequest
    template_name = "holidays/requests.html"
    context_object_name = "requests"
    paginate_by = 20


class HolidayRequestCreateView(CreateView):
    model = HolidayRequest
    form_class = HolidayRequestForm
    template_name = "holidays/request_form.html"
    success_url = reverse_lazy("holidays_index")


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
