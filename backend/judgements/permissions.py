from rest_framework.permissions import BasePermission

class IsJudgeOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write permissions are only allowed to the judge assigned to the case
        return obj.judge == request.user
