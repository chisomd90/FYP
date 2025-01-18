from django.db import models
from cases.models import Case
from accounts.models import CustomUser

class Schedule(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='schedules')
    judge = models.ForeignKey(CustomUser, limit_choices_to={'role': 'judge'}, on_delete=models.CASCADE, related_name='schedules_as_judge')
    lawyers = models.ManyToManyField(CustomUser, limit_choices_to={'role': 'lawyer'}, related_name='schedules_as_lawyers')
    clerk = models.ForeignKey(CustomUser, limit_choices_to={'role': 'clerk'}, on_delete=models.CASCADE, related_name='schedules_as_clerk')
    
    scheduled_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)  # Optional field for any additional information

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Schedule for Case {self.case.case_number} on {self.scheduled_date}"
