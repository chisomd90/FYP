from django.urls import path
from .views import DocumentListCreateView, DocumentDetailView, filter_documents

urlpatterns = [
    # URL to list all documents or create a new document
    path('documents/', DocumentListCreateView.as_view(), name='document-list-create'),

    # URL to retrieve, update, or delete a specific document
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),

    # URL for filtering documents based on tags, linked cases, or linked judgments
    path('documents/filter/', filter_documents, name='document-filter'),
]
