from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cases.views import CaseViewSet

router = DefaultRouter()
router.register('cases', CaseViewSet, basename='case')

urlpatterns = [
    path('', include(router.urls)),  # Includes all case-related routes
]
