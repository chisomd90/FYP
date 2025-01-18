from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class CustomUserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def validate(self, data):
        # Check if the username is unique
        if CustomUser.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "This username is already taken."})

        # Check if the email is unique
        if CustomUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})

        return data

    def validate_role(self, value):
        # Ensure the role is one of the predefined choices
        if value not in [choice.value for choice in CustomUser.Role]:
            raise serializers.ValidationError("Invalid role selected.")
        return value

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', CustomUser.Role.CLERK)  # Default to 'CLERK' if no role is provided
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the user to the database
        return user  # Return the user instance
