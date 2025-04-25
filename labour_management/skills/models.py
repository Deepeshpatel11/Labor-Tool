from django.db import models
from django.conf import settings


class Area(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class SkillMaster(models.Model):
    """
    A master list of all possible skills.
    """
    name = models.CharField(max_length=100, unique=True,
                            help_text="E.g. 'Forklift', 'Slicing', 'Seasoning'")

    def __str__(self):
        return self.name


class EmployeeSkill(models.Model):
    """
    The skills profile for one employee:
      - which Employee
      - their one primary skill
      - zero or more additional skills
    """
    employee = models.ForeignKey(
        "employees.Employee",
        on_delete=models.CASCADE,
        related_name="skill_profile",
        help_text="Who this skill record belongs to"
    )
    primary_skill = models.ForeignKey(
        SkillMaster,
        on_delete=models.PROTECT,
        related_name="primary_for",
        help_text="Their main skill"
    )
    additional_skills = models.ManyToManyField(
        SkillMaster,
        blank=True,
        related_name="additional_for",
        help_text="Any other skills this person has"
    )

    class Meta:
        verbose_name = "Employee Skill Matrix"
        verbose_name_plural = "Employee Skill Matrices"
        unique_together = ("employee", "primary_skill")

    def __str__(self):
        return f"{self.employee.full_name} — Primary: {self.primary_skill.name}"
