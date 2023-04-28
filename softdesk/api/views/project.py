from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from django.db.models import Q
from api.serializers.project import ProjectListSerializer, ProjectDetailSerializer
from api.models import Project
from api.permissions.is_author_or_contributor import IsAuthorOrContributor


class ProjectViewSet(ModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated, IsAuthorOrContributor]
    list_serializer = ProjectListSerializer
    retrieve_serializer = ProjectDetailSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.retrieve_serializer
        return self.list_serializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
