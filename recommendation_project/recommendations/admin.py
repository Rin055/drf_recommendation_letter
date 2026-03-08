from django.contrib import admin
from .models import *

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Skill)
admin.site.register(RecommendationRequest)
admin.site.register(RecommendationLetter)