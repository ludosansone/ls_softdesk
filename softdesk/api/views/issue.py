from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from api.models import Project, Issue
from api.serializers.project import ProjectListSerializer, ProjectDetailSerializer
from api.serializers.issue import IssueListSerializer, IssueDetailSerializer
from api.permissions.is_project_author_or_contributor import IsProjectAuthorOrContributor


class IssueViewSet(ModelViewSet, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    permission_classes = [IsAuthenticated, IsProjectAuthorOrContributor]
    list_serializer = IssueListSerializer
    retrieve_serializer = IssueDetailSerializer

    def get_queryset(self):
        return Issue.objects.all()

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
