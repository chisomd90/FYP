from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_by', 'linked_case', 'uploaded_at']
    search_fields = ['title', 'description', 'tags']
    list_filter = ['uploaded_at', 'linked_case']
