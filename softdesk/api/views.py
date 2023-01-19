from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.serializers import ProjectListSerializer, ProjectDetailSerializer
from api.models import Project


class ProjectViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    list_serializer = ProjectListSerializer
    detail_serializer = ProjectDetailSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer
        return self.list_serializer
