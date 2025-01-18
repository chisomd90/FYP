from django.db import models
from accounts.models import CustomUser

class Case(models.Model):
    case_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    plaintiff = models.CharField(max_length=255)
    defendant = models.CharField(max_length=255)
    
    # Adding related_name to avoid reverse accessor conflicts
    judge = models.ForeignKey(
        CustomUser, 
        limit_choices_to={'role': 'judge'}, 
        on_delete=models.CASCADE, 
        related_name='cases_as_judge'
    )
    
    # Adding related_name to ManyToManyField to avoid reverse accessor conflicts
    lawyer = models.ManyToManyField(
        CustomUser, 
        limit_choices_to={'role': 'lawyer'}, 
        related_name='cases_as_lawyer'
    )
    
    status = models.CharField(max_length=50, choices=[
        ('ongoing', 'Ongoing'),
        ('closed', 'Closed'),
        ('appealed', 'Appealed'),
    ])
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Case {self.case_number}: {self.title}"
