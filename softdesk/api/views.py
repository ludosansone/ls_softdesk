from rest_framework.viewsets import ModelViewSet
from api.serializers import ProjectListSerializer
from api.models import Project


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectListSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset
