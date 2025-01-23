from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Case
from .serializers import CaseSerializer

class CaseViewSet(ModelViewSet):
    """ViewSet for managing cases."""
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for access

    def list(self, request, *args, **kwargs):
        """Override list method for any custom behavior (optional)."""
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """Override retrieve method for any custom behavior (optional)."""
        return super().retrieve(request, *args, **kwargs)

    def perform_create(self, request, serializer):
        """Set the created_by field to the logged-in user when creating a case."""
        serializer.save(created_by=request.user)

    def perform_update(self, serializer):
        """Custom update logic if required (currently defaults to DRF behavior)."""
        serializer.save()

    @action(detail=True, methods=['post'], url_path='close-case')
    def close_case(self, request, pk=None):
        """Custom action to close a case."""
        case = self.get_object()
        case.status = 'closed'
        case.save()
        return Response({'status': 'Case closed'})
