from django.contrib import admin
from .models import Schedule

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['title', 'scheduled_date', 'created_by']
    search_fields = ['title', 'case__name']
    list_filter = ['scheduled_date', 'created_at']
