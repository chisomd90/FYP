from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .models import Proceeding
from .serializers import ProceedingSerializer
from .filters import ProceedingFilter

class ProceedingListCreateView(generics.ListCreateAPIView):
    queryset = Proceeding.objects.all()
    serializer_class = ProceedingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProceedingFilter
    search_fields = ['title', 'description']
    ordering_fields = ['date_recorded']
    ordering = ['-date_recorded']  # Default ordering

    def perform_create(self, serializer):
        serializer.save(recorded_by=self.request.user)

class ProceedingDetailView(generics.RetrieveAPIView):  # Use RetrieveAPIView for getting a single record
    queryset = Proceeding.objects.all()
    serializer_class = ProceedingSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProceedingDetailUpdateView(generics.UpdateAPIView):  # Added for PUT/PATCH updates
    queryset = Proceeding.objects.all()
    serializer_class = ProceedingSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProceedingDeleteView(generics.DestroyAPIView):  # Added for DELETE
    queryset = Proceeding.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        # Get the object using the lookup field (i.e., the pk)
        instance = self.get_object()
        # Call the superclass's destroy method to delete it
        self.perform_destroy(instance)
        # Return a custom success response
        return Response(
            {"message": "Proceeding successfully deleted"}, 
            status=status.HTTP_204_NO_CONTENT
        )

    def perform_destroy(self, instance):
        instance.delete()
