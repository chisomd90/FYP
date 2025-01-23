from django.urls import path
from .views import JudgementListCreateView, JudgementDetailView, filter_judgements

urlpatterns = [
    path('', JudgementListCreateView.as_view(), name='judgement-list-create'),
    path('<int:pk>/', JudgementDetailView.as_view(), name='judgement-detail'),
    path('filter/', filter_judgements, name='filter-judgements'),
]
