from django.urls import path
from .views import JudgementListCreateView, JudgementDetailView, filter_judgements

urlpatterns = [
    path('judgements/', JudgementListCreateView.as_view(), name='judgement-list-create'),
    path('judgements/<int:pk>/', JudgementDetailView.as_view(), name='judgement-detail'),
    path('judgements/filter/', filter_judgements, name='filter-judgements'),
]
