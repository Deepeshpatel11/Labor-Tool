from django.db import models
from django.conf import settings

class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    A single skill entry for an employee.
    """
    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="skills",
    )
    name = models.CharField(max_length=100, help_text="E.g. 'Forklift', 'Hygiene Champion'")

    def __str__(self):
        return f"{self.employee.full_name}: {self.name}"
