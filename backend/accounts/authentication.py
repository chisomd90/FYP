# accounts/authentication.py
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except AuthenticationFailed as e:
            raise AuthenticationFailed({"detail": "The token provided is invalid or expired."})
