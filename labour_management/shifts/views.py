import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Shift, ShiftHistory
from employees.models import Employee
from holidays.models import HolidayRequest


def index(request):
    # Handle new Shift creation via modal POST
    if request.method == 'POST':
        date_str = request.POST.get('date')
        team = request.POST.get('team')
        shift_time = request.POST.get('shift_time')
        if date_str and team and shift_time:
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            Shift.objects.get_or_create(
                date=date,
                team=team,
                shift_time=shift_time
            )
        return redirect('shifts_index')

    # GET: list upcoming shifts
    today = datetime.date.today()
    shifts = (
        Shift.objects
        .filter(date__gte=today)
        .order_by('date', 'team', 'shift_time')
    )

    # pass dropdown choices into template for modal
    context = {
        'shifts': shifts,
        'team_choices': Shift.TEAM_CHOICES,
        'shift_time_choices': Shift.TIME_CHOICES,
    }
    return render(request, 'shifts/index.html', context)


def manning_rota(request, date):
    # Parse date from URL and fetch the Shift
    shift_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    shift = get_object_or_404(Shift, date=shift_date)

    # Build employee pool: home team members not on holiday
    absent_ids = (
        HolidayRequest.objects
        .filter(start_date__lte=shift_date, end_date__gte=shift_date)
        .values_list('employee_id', flat=True)
    )
    pool = (
        Employee.objects
        .filter(active=True, shift=shift.team)
        .exclude(pk__in=absent_ids)
    )

    if request.method == 'POST':
        # Clear old assignments then save new ones
        ShiftHistory.objects.filter(shift=shift).delete()
        for key, value in request.POST.items():
            if key.startswith('assign_') and value:
                emp_pk = key.split('_', 1)[1]
                ShiftHistory.objects.create(
                    shift=shift,
                    employee_id=emp_pk
                )
        return redirect('shifts_index')

    # GET: show existing assignments
    assignments = (
        ShiftHistory.objects
        .filter(shift=shift)
        .select_related('employee')
    )

    return render(request, 'shifts/manning_rota.html', {
        'shift': shift,
        'pool': pool,
        'assignments': assignments,
    })
