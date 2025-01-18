from django.db import models
from accounts.models import CustomUser
from cases.models import Case

class Proceeding(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField()
    outcome = models.TextField(blank=True, null=True)
    judge = models.ForeignKey(CustomUser, limit_choices_to={'role': 'judge'}, on_delete=models.CASCADE)

    def __str__(self):
        return f"Proceeding for Case {self.case.case_number} on {self.date}"

