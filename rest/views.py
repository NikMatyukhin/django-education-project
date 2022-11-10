from rest_framework import viewsets, generics, mixins
from django.contrib.auth.models import User

from education_app.models import Work, Assessment

from .serializers import WorkSerializer, AssessmentSerializer, UserSerializer

# Create your views here.
class WorkViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer


class AssessmentViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer


class UserViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
