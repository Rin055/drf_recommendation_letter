from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'skills', SkillViewSet)
router.register(r'letters', RecommendationLetterViewSet)

urlpatterns = [
    path('students/', StudentListCreateAPIView.as_view()),
    path('requests/<int:pk>/', RecommendationRequestDetailAPIView.as_view()),
    path('', include(router.urls)),
]