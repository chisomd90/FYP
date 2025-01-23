from django.db import models
from django.contrib.auth import get_user_model
from cases.models import Case
from datetime import datetime

User = get_user_model()

class Proceeding(models.Model):
    title = models.CharField(max_length=255, default="Untitled")
    description = models.TextField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="proceedings")
    recorded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="recorded_proceedings")
    date_recorded = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
