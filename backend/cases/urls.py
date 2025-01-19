from django.urls import path
from .views import CaseView

urlpatterns = [
    path('cases/', CaseView.as_view(), name='case_list_create'),
    path('cases/<int:case_id>/', CaseView.as_view(), name='case_detail_update_delete'),
]
