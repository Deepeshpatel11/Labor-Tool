from django.db import models
from employees.models import Employee    # adjust import path if needed


class Area(models.Model):
    """
    A work area (e.g. Process, Primary Packaging, Palletiser, etc.).
    We keep this so you can assign or filter by area if needed.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkillMaster(models.Model):
    """
    A master list of all possible skills.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="E.g. 'Forklift', 'Slicing', 'Seasoning'"
    )

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    """
    A one-to-one “skill profile” for each employee:
      - employee (FK → Employee, from which you get name, shift, line, area)
      - primary_skill   (required)
      - secondary_skill (optional)
      - tertiary_skill  (optional)
    """
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        related_name="skill_profile",
        help_text="The employee whose skills these are"
    )
    primary_skill = models.ForeignKey(
        SkillMaster,
        on_delete=models.PROTECT,
        related_name="primary_for",
        help_text="Their main skill"
    )
    secondary_skill = models.ForeignKey(
        SkillMaster,
        on_delete=models.PROTECT,
        related_name="secondary_for",
        blank=True,
        null=True,
        help_text="Their second skill (optional)"
    )
    tertiary_skill = models.ForeignKey(
        SkillMaster,
        on_delete=models.PROTECT,
        related_name="tertiary_for",
        blank=True,
        null=True,
        help_text="Their third-level skill (optional)"
    )

    class Meta:
        verbose_name = "Employee Skill Matrix"
        verbose_name_plural = "Employee Skill Matrices"

    def __str__(self):
        return f"{self.employee.full_name} Skills"
