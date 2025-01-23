from django.urls import path
from .views import ScheduleListCreateView, ScheduleDetailView

urlpatterns = [
    path('', ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('<int:pk>/', ScheduleDetailView.as_view(), name='schedule-detail'),
]
