from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from .permissions import IsUploaderOrReadOnly

# List and Create Documents
class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

# Retrieve, Update, and Delete a Specific Document
class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsUploaderOrReadOnly]

# Filter Documents
@api_view(['GET'])
def filter_documents(request):
    tags = request.query_params.get('tags')
    case_id = request.query_params.get('linked_case')
    judgment_id = request.query_params.get('linked_judgment')

    documents = Document.objects.all()
    if tags:
        documents = documents.filter(tags__icontains=tags)
    if case_id:
        documents = documents.filter(linked_case_id=case_id)
    if judgment_id:
        documents = documents.filter(linked_judgment_id=judgment_id)

    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)
