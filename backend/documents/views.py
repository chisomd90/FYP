from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Document, Case, Judgement
from .serializers import DocumentSerializer
from .permissions import IsUploaderOrReadOnly

# List and Create Documents
class DocumentListCreateView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        document = serializer.save(uploaded_by=self.request.user)

        # Handle linking cases and judgments if provided in the request
        linked_case = self.request.data.get('linked_case', [])
        linked_judgments = self.request.data.get('linked_judgment', [])
        
        if linked_case:
            # Link the provided cases to the document
            document.linked_case.set(Case.objects.filter(id__in=linked_case))

        if linked_judgments:
            # Link the provided judgments to the document
            document.linked_judgment.set(Judgement.objects.filter(id__in=linked_judgments))

        document.save()

# Retrieve, Update, and Delete a Specific Document
class DocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [permissions.IsAuthenticated, IsUploaderOrReadOnly]

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return Response({"message": "Document deleted successfully."}, status=status.HTTP_200_OK)

# Filter Documents
@api_view(['GET'])
def filter_documents(request):
    tags = request.query_params.get('tags')
    case_id = request.query_params.get('linked_case')
    judgment_id = request.query_params.get('linked_judgment')

    documents = Document.objects.all()

    # Filter by tags if provided
    if tags:
        documents = documents.filter(tags__icontains=tags)

    # Filter by linked_case if provided
    if case_id:
        documents = documents.filter(linked_case__id=case_id)

    # Filter by linked_judgment if provided
    if judgment_id:
        documents = documents.filter(linked_judgment__id=judgment_id)

    # Serialize the filtered documents
    serializer = DocumentSerializer(documents, many=True)
    return Response(serializer.data)
