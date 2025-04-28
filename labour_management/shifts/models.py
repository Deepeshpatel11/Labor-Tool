from django.db import models
from employees.models import Employee

class Shift(models.Model):
    TEAM_CHOICES = [
        ('Red', 'Red Shift'),
        ('Green', 'Green Shift'),
        ('Blue', 'Blue Shift'),
        ('Yellow', 'Yellow Shift'),
    ]
    TIME_CHOICES = [
        ('Day', 'Day Shift'),
        ('Night', 'Night Shift'),
    ]

    date       = models.DateField()
    team       = models.CharField(max_length=10, choices=TEAM_CHOICES)
    shift_time = models.CharField(max_length=6,  choices=TIME_CHOICES)

    class Meta:
        unique_together = ('date', 'team', 'shift_time')
        ordering = ['date', 'team', 'shift_time']

    def __str__(self):
        return f"{self.date} ― {self.team} ({self.shift_time})"


class ShiftHistory(models.Model):
    shift    = models.ForeignKey(Shift,        on_delete=models.CASCADE, related_name='assignments')
    employee = models.ForeignKey(Employee,     on_delete=models.CASCADE, related_name='shifts')
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('shift', 'employee')
        ordering = ['shift', 'employee']

    def __str__(self):
        return f"{self.employee.full_name} on {self.shift}"
