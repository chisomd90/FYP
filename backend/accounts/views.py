from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserSignupSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


class SignupView(generics.CreateAPIView):
    """
    Allows new users to sign up and generates an authentication token.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSignupSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate or retrieve token for the user
        token, created = Token.objects.get_or_create(user=user)

        response_data = {
            "user": {
                "id": user.id,  # Include id for easy identification
                "username": user.username,
                "email": user.email,
                "role": user.role
            },
            "token": token.key
        }

        return Response(response_data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def role_based_dashboard(request):
    """
    Displays a role-based message to the user depending on their role.
    Accessible only to authenticated users.
    """
    # Check if the token is being recognized in the request headers
    auth_header = request.headers.get("Authorization", None)
    print("Authorization Header:", auth_header)  # Debug line
    print("User:", request.user)  # Debug line


    user = request.user
    role_messages = {
        CustomUser.Role.ADMIN: "Welcome to the Admin Dashboard!",
        CustomUser.Role.JUDGE: "Welcome to the Judge Dashboard!",
        CustomUser.Role.CLERK: "Welcome to the Clerk Dashboard!",
        CustomUser.Role.LAWYER: "Welcome to the Lawyer Dashboard!"
    }
    message = role_messages.get(user.role, "No specific dashboard for your role.")
    return Response({"message": message}, status=status.HTTP_200_OK)

class LogoutView(APIView):
    """
    Logs out the user by deleting their authentication token.
    Accessible only to authenticated users.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)
        

class RefreshTokenView(APIView):
    """
    Refreshes the authentication token for the user.
    Accessible only to authenticated users.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Get the current token
        old_token = request.auth

        if not old_token:
            return Response({"detail": "No token provided."}, status=status.HTTP_400_BAD_REQUEST)

        # Optional: Invalidate the old token (delete it)
        # old_token.delete()  # Uncomment if you want to invalidate the old token

        # Create or retrieve a new token
        new_token, created = Token.objects.get_or_create(user=request.user)

        return Response({"token": new_token.key}, status=status.HTTP_200_OK)
