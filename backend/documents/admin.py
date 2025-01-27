from django.contrib import admin
from .models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'uploaded_by', 'uploaded_at', 'display_linked_cases', 'display_linked_judgments')

    # Custom methods to display the linked cases and judgments
    def display_linked_cases(self, obj):
        return ", ".join(str(case) for case in obj.linked_case.all())
    display_linked_cases.short_description = 'Linked Cases'

    def display_linked_judgments(self, obj):
        return ", ".join(str(judgment) for judgment in obj.linked_judgment.all())
    display_linked_judgments.short_description = 'Linked Judgments'

admin.site.register(Document, DocumentAdmin)
