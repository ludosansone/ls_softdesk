from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers.project import ProjectListSerializer, ProjectDetailSerializer
from api.models import Project


class ProjectViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    list_serializer = ProjectListSerializer
    retrieve_serializer = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer
        return self.list_serializer
