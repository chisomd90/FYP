from django.urls import path
from .views import ProceedingListCreateView

urlpatterns = [
    path('', ProceedingListCreateView.as_view(), name='proceeding-list-create'),
]
