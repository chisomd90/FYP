from django.db import models
from django.contrib.auth import get_user_model
from cases.models import Case

User = get_user_model()

class Schedule(models.Model):
    case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True, related_name="schedules")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    scheduled_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="created_schedules")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.scheduled_date}"

    class Meta:
        ordering = ['scheduled_date']
