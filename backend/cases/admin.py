from django.contrib import admin
from .models import Case

class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'case_number', 'title', 'plaintiff', 'defendant', 'judge', 'status', 'created_at', 'updated_at')
    search_fields = ['case_number', 'plaintiff', 'defendant']
    list_filter = ('status', 'judge')

admin.site.register(Case, CaseAdmin)
