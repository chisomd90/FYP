from django.db import models
from django.contrib.auth import get_user_model
from cases.models import Case
from judgements.models import Judgement

User = get_user_model()

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="documents/", null=True, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="uploaded_documents")
    linked_case = models.ForeignKey(Case, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents")
    linked_judgment = models.ForeignKey(Judgement, on_delete=models.SET_NULL, null=True, blank=True, related_name="documents")
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags for searching")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uploaded_at']
