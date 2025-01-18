from django.db import models
from accounts.models import CustomUser
from cases.models import Case

class Judgment(models.Model):
    case = models.OneToOneField(Case, on_delete=models.CASCADE)
    judge = models.ForeignKey(CustomUser, limit_choices_to={'role': 'judge'}, on_delete=models.CASCADE)
    judgment_text = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Judgment for Case {self.case.case_number}"
