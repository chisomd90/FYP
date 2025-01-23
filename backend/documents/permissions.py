from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsUploaderOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed for the uploader
        return obj.uploaded_by == request.user
