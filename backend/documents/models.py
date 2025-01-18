from django.db import models
from accounts.models import CustomUser
from cases.models import Case

class Document(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document = models.FileField(upload_to='case_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.document_name} for Case {self.case.case_number}"

