from django.urls import path
from . import views
from accounts.views import LogoutView, SignupView
from rest_framework.authtoken.views import  obtain_auth_token

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('dashboard/', views.role_based_dashboard, name='role_based_dashboard'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('refresh-token/', views.RefreshTokenView.as_view(), name='refresh_token'),
]
