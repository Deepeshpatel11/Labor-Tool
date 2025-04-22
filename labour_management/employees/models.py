from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Employee(models.Model):
    # link to Django’s built‑in User
    full_name = models.CharField(max_length=100, unique=True)
    gpid      = models.CharField(max_length=20, unique=True)

    # four‑colour shift cycle
    SHIFT_GREEN  = "Green"
    SHIFT_BLUE   = "Blue"
    SHIFT_RED    = "Red"
    SHIFT_YELLOW = "Yellow"
    SHIFT_CHOICES = [
        (SHIFT_GREEN,  "Green"),
        (SHIFT_BLUE,   "Blue"),
        (SHIFT_RED,    "Red"),
        (SHIFT_YELLOW, "Yellow"),
    ]
    shift = models.CharField(
        max_length=10,
        choices=SHIFT_CHOICES,
        default=SHIFT_GREEN,
    )

    # add Role choices
    ROLE_GSO = "GSO"
    ROLE_GO  = "GO"
    ROLE_MT  = "MT"
    ROLE_ST  = "ST"
    ROLE_CHOICES = [
        (ROLE_GSO, "General Support Operator"),
        (ROLE_GO,  "General Operator"),
        (ROLE_MT,  "Manufacturing Technician"),
        (ROLE_ST,  "Shift Technician"),
    ]
    role = models.CharField(
        max_length=3,
        choices=ROLE_CHOICES,
        default=ROLE_GSO,
        help_text="What type of role this person performs",
    )

    # production line assignment (plus MOH & ALL)
    LINE_1   = "1"
    LINE_2   = "2"
    LINE_3   = "3"
    LINE_4   = "4"
    LINE_MOH = "MOH"
    LINE_ALL = "ALL"
    LINE_CHOICES = [
        (LINE_1,   "Line 1"),
        (LINE_2,   "Line 2"),
        (LINE_3,   "Line 3"),
        (LINE_4,   "Line 4"),
        (LINE_MOH, "MOH"),
        (LINE_ALL, "ALL"),
    ]
    line = models.CharField(
        max_length=10,
        choices=LINE_CHOICES,
        default=LINE_1,
        help_text="Which line (or MOH/ALL) the employee normally works",
    )

    # work area FK into skills app
    area   = models.ForeignKey("skills.Area", on_delete=models.PROTECT)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.full_name} ({self.gpid})"
