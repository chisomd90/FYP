from django.db import models
from cases.models import Case
from accounts.models import CustomUser

class Judgement(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name="judgements")
    judge = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="judgements")
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_of_judgment = models.DateField()
    references = models.TextField(blank=True, null=True, help_text="References or citations used in this judgment")
    attachments = models.FileField(upload_to='judgements/', blank=True, null=True, help_text="Additional documents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - Case: {self.case}"

    class Meta:
        ordering = ['-date_of_judgment']
