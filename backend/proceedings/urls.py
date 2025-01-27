from django.urls import path
from .views import ProceedingListCreateView, ProceedingDetailView, ProceedingDetailUpdateView, ProceedingDeleteView

urlpatterns = [
    path('proceedings/', ProceedingListCreateView.as_view(), name='proceeding-list-create'),
    path('proceedings/<int:pk>/', ProceedingDetailView.as_view(), name='proceeding-detail'),
    path('proceedings/update/<int:pk>/', ProceedingDetailUpdateView.as_view(), name='proceeding-update'),
    path('proceedings/delete/<int:pk>/', ProceedingDeleteView.as_view(), name='proceeding-delete'),
]
