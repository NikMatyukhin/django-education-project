from rest_framework import viewsets

from education_app.models import Work

from .serializers import WorkSerializer

# Create your views here.
class WorkViewset(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
