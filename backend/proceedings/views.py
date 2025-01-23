from rest_framework import generics, permissions, filters
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
