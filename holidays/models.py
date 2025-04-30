from django.db import models
from employees.models import Employee


class HolidayRequest(models.Model):
    STATUS_PENDING = "Pending"
    STATUS_APPROVED = "Approved"
    STATUS_REJECTED = "Rejected"
    STATUS_CHOICES = [
        (STATUS_PENDING,  "Pending"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="holiday_requests"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )
    requested_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        return (
            f"{self.employee.full_name}: "
            f"{self.start_date}–{self.end_date} ({self.status})"
        )
