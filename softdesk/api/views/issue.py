from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.models import Project, Issue
from api.serializers.project import ProjectListSerializer, ProjectDetailSerializer
from api.serializers.issue import IssueListSerializer, IssueDetailSerializer


class IssueViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    list_serializer = IssueListSerializer
    retrieve_serializer = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer
        return self.list_serializer
