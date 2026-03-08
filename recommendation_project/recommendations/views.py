from rest_framework import generics, mixins, viewsets
from .models import Student, Professor, Skill, RecommendationRequest, RecommendationLetter
from .serializers import StudentSerializer, ProfessorSerializer, SkillSerializer, RecommendationRequestSerializer, RecommendationLetterSerializer


class StudentListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProfessorListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RecommendationRequestListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = RecommendationRequest.objects.all()
    serializer_class = RecommendationRequestSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RecommendationRequestDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = RecommendationRequest.objects.all()
    serializer_class = RecommendationRequestSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SkillViewSet(viewsets.ModelViewSet):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get', 'post', 'delete']


class RecommendationLetterViewSet(viewsets.ModelViewSet):

    queryset = RecommendationLetter.objects.all()
    serializer_class = RecommendationLetterSerializer