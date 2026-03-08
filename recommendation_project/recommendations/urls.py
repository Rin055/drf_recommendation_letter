from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'letters', RecommendationLetterViewSet)

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('professors/', ProfessorListCreateAPIView.as_view(), name='professor-list-create'),
    path('requests/', RecommendationRequestListCreateAPIView.as_view(), name='request-list-create'),
    path('requests/<int:pk>/', RecommendationRequestDetailAPIView.as_view(), name='request-detail'),
    path('', include(router.urls)),
]