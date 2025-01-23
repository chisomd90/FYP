from django.urls import path
from .views import DocumentListCreateView, DocumentDetailView, filter_documents

urlpatterns = [
    path('', DocumentListCreateView.as_view(), name='document-list-create'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('filter/', filter_documents, name='document-filter'),
]
