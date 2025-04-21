from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    gpid    = models.CharField(max_length=20)
    shift   = models.CharField(max_length=10)    # “Day” or “Night”
    role    = models.CharField(max_length=100)
    area    = models.CharField(max_length=100)
    active  = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.gpid})"

class Skill(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    name     = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.employee}: {self.name}"

class HolidayRequest(models.Model):
    employee   = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date   = models.DateField()
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]
    status     = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"{self.employee} {self.start_date}→{self.end_date} [{self.get_status_display()}]"

class Shift(models.Model):
    date         = models.DateField()
    shift_type   = models.CharField(max_length=10)   # “Day”/“Night”
    scenario1    = models.CharField(max_length=50, blank=True)
    scenario2    = models.CharField(max_length=50, blank=True)
    scenario3    = models.CharField(max_length=50, blank=True)
    scenario4    = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.date} {self.shift_type}"

class ManningAssignment(models.Model):
    shift       = models.ForeignKey(Shift, on_delete=models.CASCADE)
    line_number = models.PositiveSmallIntegerField()
    scenario    = models.CharField(max_length=50)
    sub_area    = models.CharField(max_length=100)
    role        = models.CharField(max_length=100)
    employee    = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    hours       = models.DecimalField(max_digits=4, decimal_places=1)

    def __str__(self):
        return f"{self.shift} L{self.line_number} {self.scenario} → {self.employee}"
