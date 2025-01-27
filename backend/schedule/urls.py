from django.urls import path
from .views import ScheduleListCreateView, ScheduleDetailView

urlpatterns = [
    path('schedule/', ScheduleListCreateView.as_view(), name='schedule-list-create'),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name='schedule-detail'),
]
