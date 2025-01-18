from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # Removed 'role' from fields


class AdminSignUpForm(CustomUserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields + ['first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'admin'  # Automatically set the role to 'admin'
        if commit:
            user.save()
        return user


class JudgeSignUpForm(CustomUserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields + ['first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'judge'  # Automatically set the role to 'judge'
        if commit:
            user.save()
        return user


class ClerkSignUpForm(CustomUserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields + ['first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'clerk'  # Automatically set the role to 'clerk'
        if commit:
            user.save()
        return user


class LawyerSignUpForm(CustomUserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser
        fields = CustomUserCreationForm.Meta.fields + ['first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'lawyer'  # Automatically set the role to 'lawyer'
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
