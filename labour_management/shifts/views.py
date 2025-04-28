import datetime
from django.shortcuts import render, get_object_or_404, redirect
from .models import Shift, ShiftHistory
from employees.models import Employee
from holidays.models import HolidayRequest
from .forms import ShiftAssignmentForm, SCENARIO_CONFIG

def index(request):
    if request.method == 'POST':
        d = request.POST.get('date')
        t = request.POST.get('team')
        s = request.POST.get('shift_time')
        if d and t and s:
            dt = datetime.datetime.strptime(d, '%Y-%m-%d').date()
            Shift.objects.get_or_create(date=dt, team=t, shift_time=s)
        return redirect('shifts_index')

    today  = datetime.date.today()
    shifts = Shift.objects.filter(date__gte=today)
    return render(request, 'shifts/index.html', {
        'shifts':             shifts,
        'team_choices':       Shift.TEAM_CHOICES,
        'shift_time_choices': Shift.TIME_CHOICES,
    })


def manning_rota(request, date):
    # parse date and fetch shift
    dt    = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    shift = get_object_or_404(Shift, date=dt)

    # which line & scenario
    line     = request.GET.get('line', 'line1')
    scenario = request.GET.get('scenario', 'pc_production')

    # handle form submit
    if request.method == 'POST':
        form = ShiftAssignmentForm(request.POST, shift=shift, line=line, scenario=scenario)
        if form.is_valid():
            ShiftHistory.objects.filter(shift=shift).delete()
            for emp_pk in form.cleaned_data.values():
                if emp_pk:
                    ShiftHistory.objects.create(shift=shift, employee_id=emp_pk)
            return redirect('shifts_index')
    else:
        form = ShiftAssignmentForm(shift=shift, line=line, scenario=scenario)

    # build simple lists for template
    lines_list     = list(SCENARIO_CONFIG.keys())
    scenarios_list = list(SCENARIO_CONFIG.get(line, {}).keys())

    return render(request, 'shifts/manning_rota.html', {
        'shift':      shift,
        'form':       form,
        'line':       line,
        'scenario':   scenario,
        'lines':      lines_list,
        'scenarios':  scenarios_list,
        'SCENARIO_CONFIG': SCENARIO_CONFIG,
    })
