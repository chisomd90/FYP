from django_filters import rest_framework as filters
from .models import Proceeding

class ProceedingFilter(filters.FilterSet):
    date_range = filters.DateFromToRangeFilter(field_name="date_recorded")

    class Meta:
        model = Proceeding
        fields = ['case', 'recorded_by', 'date_range']
