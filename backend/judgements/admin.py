from django.contrib import admin
from .models import Judgement

# Optionally, customize the admin interface
class JudgementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'case', 'judge', 'date_of_judgment', 'created_at')
    list_filter = ('date_of_judgment', 'judge', 'case')
    search_fields = ('title', 'content', 'references', 'case__title', 'judge__username')

# Register the Judgement model
admin.site.register(Judgement, JudgementAdmin)
