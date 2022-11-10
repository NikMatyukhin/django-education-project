from rest_framework import viewsets, generics, mixins, response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from django.db.models import Sum, Max, F

from education_app.models import Work, Assessment

from .serializers import WorkSerializer, AssessmentSerializer, UserSerializer

# Create your views here.
class WorkViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    @action(methods=['get'], detail=False, url_path='best-works')
    def best_works(self, request):
        works = (
            Work.objects
            .annotate(score_sum=Sum('assessments__score'))
            .order_by('-score_sum')[:3]
        )
        serializer = WorkSerializer(works, many=True)
        return response.Response(data=serializer.data)


# class AssessmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
