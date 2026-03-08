from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class RecommendationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationRequest
        fields = '__all__'

class RecommendationLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendationLetter
        fields = '__all__'