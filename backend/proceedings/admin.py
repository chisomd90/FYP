from django.contrib import admin
from .models import Proceeding

class ProceedingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'case', 'recorded_by', 'date_recorded')
    list_filter = ('case', 'recorded_by', 'date_recorded')
    search_fields = ('title', 'description', 'case__title', 'recorded_by__username')
    ordering = ('-date_recorded',)

admin.site.register(Proceeding, ProceedingAdmin)
