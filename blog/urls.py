from django.urls import path
from .views import PersonListCreateAPIView, PersonRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('api/persons/', PersonListCreateAPIView.as_view(), name='person-list-create'),
    path('api/persons/<int:pk>/', PersonRetrieveUpdateDeleteAPIView.as_view(), name='person-detail'),
]
