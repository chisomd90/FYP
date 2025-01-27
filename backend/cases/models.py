from django.db import models
from accounts.models import CustomUser

class Case(models.Model):
    case_number = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    plaintiff = models.CharField(max_length=255)
    defendant = models.CharField(max_length=255)
    judge = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="judged_cases"
    )
    lawyer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="lawyer_cases",
        null=True,  # Allows null values for the field
        blank=True  # Makes the field optional in forms
    )
    status = models.CharField(max_length=50, choices=[('ongoing', 'Ongoing'), ('closed', 'Closed')])
    created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="created_cases",
        null=False,  # Ensure field is non-nullable
        default=1    # Replace with the default user's ID
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Case {self.case_number}: {self.title}"
